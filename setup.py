#!/usr/bin/env python

from setuptools import setup

f=open('walkingliberty/__init__.py','r')
for line in f:
    if line.startswith('__version__'):
        v = line.replace("'", '').split('=')
        break
f.close()

VERSION=v[1].replace('\n','')

DOWNLOAD_URL = 'https://github.com/teran-mckinney/walkingliberty-python/tarball/{}'

DESCRIPTION = 'Basic, stateless wallet using HD type 1.'

setup(
    python_requires='>=3.3',
    name='walkingliberty',
    version=VERSION,
    author='Teran McKinney',
    author_email='sega01@go-beyond.org',
    description=DESCRIPTION,
    keywords=['bitcoin', 'bitcoincash'],
    license='Unlicense',
    url='https://github.com/teran-mckinney/walkingliberty-python',
    download_url=DOWNLOAD_URL.format(VERSION),
    packages=['walkingliberty'],
    install_requires=[
        'bit',
        'bitcash',
        'pyqrcode'
    ],
    entry_points={
        'console_scripts': [
            'walkingliberty = walkingliberty.cli:main',
        ]
    }
)
