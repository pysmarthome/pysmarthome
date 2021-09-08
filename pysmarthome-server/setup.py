from setuptools import setup, find_packages

setup(
    name='pysmarthome_server',
    description='A simple yet powerful python http server that integrates some smart devices',
    version='0.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'ariadne',
        'flask',
        'flask_restful',
        'pysmarthome~=2.0',
        's3db',
    ],
    packages=find_packages(),
    scripts=['pysmarthome.wsgi'],
    url='https://github.com/filipealvesdef/pysmarthome/tree/master/pysmarthome-server',
    zip_safe=False,
)
