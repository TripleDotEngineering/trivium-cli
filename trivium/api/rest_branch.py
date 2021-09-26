#!/usr/bin/env python
"""
api/rest_branch.py

Copyright 2021 Triple Dot Engineering LLC

Defines the RestBranch class used to interact with branches via the API.
"""
from ._abc_rest_obj import RestObject

class RestBranch(RestObject):
    """
    REST API branches
    """

    ##
    # RestBranch constructor
    ##
    def __init__(self, data):
        super().__init__()
        self._data = data
