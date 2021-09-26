#!/usr/bin/env python
"""
api/__init__.py

Copyright 2021 Triple Dot Engineering LLC

Initializes the API package.
"""
# Disabling due to aliases
# pylint: disable=invalid-name

from .api import TriviumApi
from .rest_user import RestUser
from .rest_organization import RestOrg
from .rest_project import RestProject
from .rest_element import RestElement

# Aliases
user = RestUser
org = RestOrg
project = RestProject
element = RestElement
test = TriviumApi().test
version = TriviumApi().version
