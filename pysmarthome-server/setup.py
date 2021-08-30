from setuptools import setup, find_packages

setup(
    name='pysmarthome_server',
    description='A simple python http server that integrates some smart devices',
    version='0.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'flask',
        'flask_restful',
        'pysmarthome_lib',
        's3db',
    ],
    packages=find_packages(),
    scripts=['pysmarthome.wsgi'],
    url='https://github.com/filipealvesdef/pysmarthome',
    zip_safe=False,
)
