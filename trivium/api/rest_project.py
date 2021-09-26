#!/usr/bin/env python
"""
api/rest_project.py

Copyright 2021 Triple Dot Engineering LLC

Defines the RestProject class used to interact with projects via the API.
"""
from ._abc_rest_obj import RestObject
from .api import TriviumApi


class RestProject(RestObject):
    """Represents a project returned from the REST API."""

    def __init__(self, data):
        super().__init__()
        self._data = data

    ##
    # Gets a single project
    ##
    @staticmethod
    def get(model, element=None, params=None):
        """Gets one or more elements"""
        parameters = params if params is not None else {}
        # Break up model identifier into parts
        ids = model.split(':')
        org = ids[0]
        project = ids[1]

        url = '/orgs/{}/projects/{}'.format(org, project)
        if element is not None:
            url += '/{}'.format(element)
        r = TriviumApi().make_request(url, params=parameters)
        if r.status_code == 200:
            return r.json()

        # If not 200, raise exception
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))
