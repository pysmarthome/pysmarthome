from setuptools import setup, find_packages

setup(
    name='pysmarthome-pc',
    description='Pc plugin for pysmarthome',
    version='1.0.2',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome~=2.0',
        'requests',
        'wakeonlan',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_pc',
    zip_zafe=False,
)
