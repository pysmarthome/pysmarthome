from setuptools import setup, find_packages

setup(
    name='pysmarthome_yeelight',
    description='Yeelight plugin for pysmarthome',
    version='1.0.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome_lib',
        'yeelight',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_yeelight',
    zip_zafe=False,
)