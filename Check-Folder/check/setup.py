from setuptools import setup

setup(
    name = 'check',
    version = '0.1.0',
    packages = ['check'],
    entry_points = {
        'console_scripts': [
            'check = check.__main__:main'
        ]
    })