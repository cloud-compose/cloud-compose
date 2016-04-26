import os
from setuptools import setup, find_packages
import warnings

setup(
    name='cloud-compose',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        "console_scripts": [
            "cloud-compose=cloudcompose.commands.main:main",
        ]
    },
    author="Patrick Cullen and the WaPo platform tools team",
    author_email="opensource@washingtonpost.com",
    url="https://github.com/cloud-compose/cloud-compose"
)
