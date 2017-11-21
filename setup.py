#!/usr/bin/env python

from setuptools import setup

VERSION = '0.1.1'

DOWNLOAD_URL = 'https://github.com/teran-mckinney/walkingliberty-python/tarball/{}'

DESCRIPTION = 'Basic, stateless wallet using HD type 1.'

setup(
    name='walkingliberty',
    version=VERSION,
    author='Teran McKinney',
    author_email='sega01@go-beyond.org',
    description=DESCRIPTION,
    keywords=['bitcoin', 'wallet'],
    license='Unlicense',
    url='https://github.com/teran-mckinney/walkingliberty-python',
    download_url=DOWNLOAD_URL.format(VERSION),
    packages=['walkingliberty'],
    install_requires=[
        'pyyaml',
        'pybitcoin>=0.9.10',
        'jsonrpclib-pelix'
    ],
    entry_points={
        'console_scripts': [
            'walkingliberty = walkingliberty.cli:main',
        ]
    }
)
