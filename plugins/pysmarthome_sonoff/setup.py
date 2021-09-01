from setuptools import setup, find_packages

setup(
    name='pysmarthome-sonoff',
    description='Sonoff plugin for pysmarthome',
    version='1.0.1',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome_lib',
        'sonoffreq',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/plugins/pysmarthome_sonoff',
    zip_zafe=False,
)
