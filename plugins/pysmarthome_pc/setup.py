from setuptools import setup, find_packages

setup(
    name='pysmarthome-pc',
    description='Pc plugin for pysmarthome',
    version='1.0.1',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome_lib',
        'requests',
        'wakeonlan',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_pc',
    zip_zafe=False,
)
