from setuptools import setup, find_packages

setup(
    name='pysmarthome',
    description='A simple python http server that integrates some smart devices',
    version='0.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'asyncio',
        'broadlink',
        'Cerberus',
        'flask',
        'flask_restful',
        'govee_api2',
        'requests',
        'sonoffreq',
        'wakeonlan',
        'yeelight',
    ],
    packages=find_packages(),
    scripts=['pysmarthome.wsgi'],
    url='https://github.com/filipealvesdef/pysmarthome',
    zip_safe=False,
)
