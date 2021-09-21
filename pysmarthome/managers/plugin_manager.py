from bs4 import BeautifulSoup
from functools import reduce
import re
import requests
import subprocess
import pkg_resources
from ..controllers import PluginController


class PluginManager:
    exclude_list = ['pysmarthome-server', 'pysmarthome-lib', 'pysmarthome']
    _db = None
    plugins = {}


    @property
    @classmethod
    def db(cls):
        return cls._db


    @db.setter
    @staticmethod
    def db(cls, conn):
        cls._db = conn


    @classmethod
    def init(cls, db, handlers={}):
        PluginManager.db = db
        plugins = PluginManager.sync_plugins_with_db()
        for name, handler in handlers.items():
            if name in cls.__dict__:
                setattr(cls, name, handler)
                continue
        for plugin in plugins:
            if plugin.active:
                plugin.init()
            cls.plugins[plugin.id] = plugin
        return PluginManager.get_controllers()


    @staticmethod
    def sync_plugins_with_db():
        print('syncing plugins...')
        installed = PluginManager.get_installed()
        db_plugins = PluginController.load_all(PluginManager.db)

        installed_names = [p['module_name'] for p in installed]
        db_names = [p.module_name for p in db_plugins]

        to_install = [p for p in db_names if p not in installed_names]
        if to_install:
            print('installing: ', *to_install)
            subprocess.run(['pip', 'install', '-q', *to_install])

        to_uninstall = [p for p in installed_names if p not in db_names]
        if to_uninstall:
            print('uninstalling: ', *to_uninstall)
            subprocess.run(['pip', 'uninstall', '-q', '-y', *to_uninstall])
        return db_plugins


    @staticmethod
    def get_installed():
        plugins = [ p for p in pkg_resources.WorkingSet() if
            p.project_name.startswith('pysmarthome-') and
            p.project_name not in PluginManager.exclude_list ]
        installed_plugins = []
        for p in plugins:
            name = p.project_name
            version = p.version
            metadata = [ m for m in p.get_metadata('PKG-INFO').split('\n')
                if m.startswith('Summary') ]
            description = metadata.pop().split(': ')[1]
            installed_plugins.append({
                'module_name': name,
                'description': description,
                'version': version,
            })
        return installed_plugins


    @staticmethod
    def search(query=''):
        url = 'https://pypi.org/search'
        r = requests.get(url, params={'q': 'pysmarthome-'})
        soup = BeautifulSoup(r.text, 'html.parser')
        snippets = soup.select('a[class*="snippet"]')
        packages = []

        for s in snippets:
            name = s.select_one('span[class*="name"]').text
            if name in PluginManager.exclude_list or\
                (query and not re.match(query, name)):
                continue

            description = s.select_one('p[class*="description"]').text
            version = s.select_one('span[class*="version"]').text
            packages.append({
                'module_name': name,
                'description': description,
                'version': version,
            })

        return packages


    @staticmethod
    def install(*plugin_names):
        query = reduce(lambda x, y: f'{x}|{y}', plugin_names)
        plugins_data = PluginManager.search(query=query)
        installed = [p['module_name'] for p in PluginManager.get_installed()]
        success = {}
        for data in plugins_data:
            module_name = data['module_name']
            success[module_name] = True
            if module_name in installed:
                success[module_name] = False
                continue
            p = PluginController.create(PluginManager.db, **data)
            subprocess.run(['pip', 'install', '-q', p.module_name])
        PluginManager.on_install(**success)


    @staticmethod
    def on_install(**installed):
        pass


    @staticmethod
    def uninstall(*ids):
        db_ids = [ p.id for p in PluginManager.plugins.values() ]
        success = {}
        for id in ids:
            success[id] = True
            if id not in db_ids:
                success[id] = False
                continue
            p = PluginManager.plugins[id]
            p.delete()
            subprocess.run(['pip', 'uninstall', '-y', '-q', p.module_name])
        PluginManager.on_uninstall(**success)


    @staticmethod
    def on_uninstall(**uninstalled):
        pass


    @staticmethod
    def toggle_active(*ids):
        plugins = [p for p in PluginManager.plugins.values() if p.id in ids]
        success = dict([(id, False) for id in ids])
        for p in plugins:
            success[p.id] = True
            p.toggle_active()
        PluginManager.on_toggle_active(**success)


    @staticmethod
    def on_toggle_active(**toggled):
        pass


    @staticmethod
    def get_controllers(plugin_id=''):
        if plugin_id:
            return PluginManager.plugins[plugin_id].controllers
        controllers = {}
        for plugin in PluginManager.plugins.values():
            controllers |= plugin.controllers
        return controllers
