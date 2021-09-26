#!/usr/bin/env python
################################################################################
#
# setup.py
#
# Copyright (c) 2021, Triple Dot Engineering LLC
#
# This file defines the package installation.
#
################################################################################
import setuptools

with open('./README.md') as fh:
    long_description = fh.read()

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='trivium-cli',
    version='0.1.0',
    description='Trivium CLI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Triple Dot Engineering',
    author_email='pypi@triple.engineer',
    url='https://triple.engineering',
    packages=[
        'trivium',
        'trivium.cli',
        'trivium.api',
        'trivium.egesters',
        'trivium.ingesters',
        'trivium.util'
    ],
    license="MIT",
    install_requires=requirements,
    package_dir={'trivium': 'trivium'},
    scripts=['scripts/trivium'],
    python_requires=">=3.6"
)
