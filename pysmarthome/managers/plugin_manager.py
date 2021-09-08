from bs4 import BeautifulSoup
from functools import reduce
import re
import requests
import subprocess
import pkg_resources
from ..controllers import PluginController


class PluginManager:
    exclude_list = ['pysmarthome-server', 'pysmarthome-lib']
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
    def init(cls, db):
        PluginManager.db = db
        plugins = PluginManager.sync_plugins_with_db()
        for plugin in plugins:
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
    def install(*plugin_names, callback_func=lambda: None):
        query = reduce(lambda x, y: f'{x}|{y}', plugin_names)
        plugins_data = PluginManager.search(query=query)
        installed = [p['module_name'] for p in PluginManager.get_installed()]
        for data in plugins_data:
            if 'module_name' not in data or data['module_name'] in installed:
                print(data['module_name'] + ' is already installed!')
                continue
            print(f'Installing ' + data['module_name'])
            p = PluginController.create(PluginManager.db, **data)
            subprocess.run(['pip', 'install', '-q', p.name])
        callback_func()


    @staticmethod
    def uninstall(*ids, callback_func=lambda: None):
        db_ids = [ p.id for p in PluginManager.plugins.values() ]
        for id in ids:
            if id not in db_ids:
                print(id + ' is not installed!')
                continue
            p = PluginManager.plugins[id]
            p.delete()
            print(f'Uninstalling ' + p.module_name)
            subprocess.run(['pip', 'uninstall', '-y', '-q', p.module_name])
        callback_func()


    @staticmethod
    def get_controllers(plugin_id=''):
        if plugin_id:
            return PluginManager.plugins[plugin_id].controllers
        controllers = {}
        for plugin in PluginManager.plugins.values():
            controllers |= plugin.controllers
        return controllers
