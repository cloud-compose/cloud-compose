import os
from setuptools import setup, find_packages
import warnings

setup(
    name='cloud-compose',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=6.6',
    ],
    entry_points={
        "console_scripts": [
            "cloud-compose=cloudcompose.cli:cli",
        ]
    },
    namespace_packages = ['cloudcompose'],
    author="Patrick Cullen and the WaPo platform tools team",
    author_email="opensource@washingtonpost.com",
    url="https://github.com/cloud-compose/cloud-compose",
    download_url = "https://github.com/cloud-compose/cloud-compose/tarball/v0.3.0",
    keywords = ['cloud', 'compose', 'aws'],
    classifiers = []
)
