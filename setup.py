from setuptools import setup, find_packages

setup(
    name='pysmarthome',
    description='A python library that aims to provide utilities to implement smart home systems',
    version='2.3.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'durc',
        'bs4',
        'requests',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/',
    zip_safe=False,
)
