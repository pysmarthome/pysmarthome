from setuptools import setup, find_packages

setup(
    name='pysmarthome-govee',
    description='Govee plugin for pysmarthome',
    version='1.0.2',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'govee_api2',
        'pysmarthome~=2.0',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_govee',
    zip_zafe=False,
)
