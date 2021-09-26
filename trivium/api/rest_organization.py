#!/usr/bin/env python
"""
api/rest_organization.py

Copyright 2021 Triple Dot Engineering LLC

Defines the RestOrg class used to interact with organizations via the API.
"""
import json
from .. import util
from ._abc_rest_obj import RestObject
from .api import TriviumApi


class RestOrg(RestObject):
    """Class for interacting with Orgs via REST api"""

    ##
    # RestOrg constructor
    ##
    def __init__(self, data):
        super().__init__()
        self._data = data

    ##
    # Returns the string representation of an organization
    ##
    def __repr__(self):
        return self.__str__()

    ##
    # Returns the string representation of an organization
    ##
    def __str__(self):
        return json.dumps(self._data, indent=4)


    ##
    # Takes a list of organizations as input and prints them in tabular format.
    ##
    @staticmethod
    def print_table(orgs):
        """Prints in tabular format."""
        fmt = '{id:20s} {name:32s}'
        labels = {
            'id': 'ID',
            'name':   'Name'
        }
        header_fmt = util.Colors.CYAN + util.Colors.BOLD
        print(header_fmt + fmt.format(**labels) + util.Colors.ENDC)

        for org in orgs:
            print(fmt.format(**org))


    ##
    # Gets a single org is the org id is provided, otherwise gets all orgs
    # that the user has access to.
    ##
    @staticmethod
    def get(org=None):
        """Gets one or more orgs"""
        url = '/orgs' if org is None else '/orgs/{}'.format(org)
        r = TriviumApi().make_request(url)
        if r.status_code == 200:
            return r.json()

        # If not 200, raise exception
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Posts an organization based on the input data.
    ##
    @staticmethod
    def post(data):
        """Posts an org"""
        opts = {
            'method': 'POST',
            'params': {},
            'body': data
        }
        r = TriviumApi().make_request('/orgs', **opts)
        if r.status_code == 200:
            return r.json()
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Deletes an organization.
    ##
    @staticmethod
    def delete(identifier):
        """Deletes orgs"""
        opts = {
            'method': 'DELETE',
            'params': {}
        }
        url = '/orgs/{0}'.format(identifier)
        r = TriviumApi().make_request(url, **opts)
        if r.status_code == 200:
            return r.json()

        # if not 200
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))

    ##
    # Patches organization(s)
    ##
    @staticmethod
    def patch(data):
        """Patches orgs"""
        opts = {
            'method': 'PATCH',
            'params': {},
            'body': data
        }
        r = TriviumApi().make_request('/orgs', **opts)
        if r.status_code == 200:
            return r.json()
        # if not 200
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))
