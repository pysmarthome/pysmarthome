from setuptools import setup, find_packages

setup(
    name='pysmarthome_lib',
    description='A python lib that abstracts pysmarthome entities',
    version='0.1.5',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'vesla_pymvc',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/pysmarthome-lib',
    zip_safe=False,
)
