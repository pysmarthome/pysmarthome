from setuptools import setup, find_packages

setup(
    name='pysmarthome_govee',
    description='Govee plugin for pysmarthome',
    version='1.0.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'govee_api2',
        'pysmarthome_lib',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_govee',
    zip_zafe=False,
)
