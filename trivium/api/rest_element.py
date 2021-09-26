#!/usr/bin/env python
"""
api/rest_element.py

Copyright 2021 Triple Dot Engineering LLC

Defines the RestElement class used to interact with elements via the API.
"""
import json
from .. import util
from ._abc_rest_obj import RestObject
from .api import TriviumApi


class RestElement(RestObject):
    """
    REST API class for elements endpoints
    """

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
    # Takes a list of elements as input and prints them in tabular format.
    ##
    @staticmethod
    def print_table(_elements):
        """Prints a table of elements"""
        # Remove newlines
        estring = json.dumps(_elements)
        elements = json.loads(estring.replace('\\n', ''))

        # Prepare for formatting
        longest = {
            'type': 10,
            'id':   32,
            'name': 24,
            'documentation': 32
        }
        for el in elements:
            for t in longest.items():
                if len(el[t]) > longest[t]:
                    longest[t] = len(el[t])
        for t in longest:
            longest[t] += 3


        fmt = []
        for t in longest.items():
            fmt.append('{' + '{}:{}s'.format(t, longest[t]) + '}')
        fmt = ' '.join(fmt)
        labels = {
            'id':       'ID',
            'name':     'Name',
            'type':     'Type',
            'documentation': 'Documentation'
        }
        header_fmt = util.Colors.CYAN + util.Colors.BOLD
        print(header_fmt + fmt.format(**labels) + util.Colors.ENDC)

        for el in elements:
            print(fmt.format(**el))


    @staticmethod
    def get(model, element=None, params=None):
        """
        Gets one or more elements
        """
        parameters = params if params is not None else {}
        # Break up model identifier into parts
        ids = model.split(':')
        org = ids[0]
        project = ids[1]
        if len(ids) > 2:
            branch = ids[2]
        else:
            branch = 'main'

        url = '/orgs/{}/projects/{}/branches/{}/elements'.format(org, project, branch)
        if element is not None:
            url += '/{}'.format(element)
        r = TriviumApi().make_request(url, params=parameters)
        if r.status_code == 200:
            return r.json()

        # If not 200, raise exception
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Posts element to a model
    ##
    @staticmethod
    def post(model, data):
        """Posts element data"""
        # Break up model identifier into parts
        ids = model.split(':')
        org = ids[0]
        project = ids[1]
        if len(ids) > 2:
            branch = ids[2]
        else:
            branch = 'main'

        opts = {
            'method': 'POST',
            'params': {'fields': 'id', 'minified': 'true'},
            'body': data
        }
        url = '/orgs/{}/projects/{}/branches/{}/elements'.format(org, project, branch)
        r = TriviumApi().make_request(url, **opts)
        if r.status_code == 200:
            return r.json()

        # If not 200, raise error
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Puts elements in a model
    ##
    @staticmethod
    def put(model, data):
        """PUT data into model"""
        # Break up model identifier into parts
        ids = model.split(':')
        org = ids[0]
        project = ids[1]
        if len(ids) > 2:
            branch = ids[2]
        else:
            branch = 'main'

        opts = {
            'method': 'PUT',
            'params': {'fields': 'id', 'minified': 'true'},
            'body': data
        }
        url = '/orgs/{}/projects/{}/branches/{}/elements'.format(org, project, branch)
        r = TriviumApi().make_request(url, **opts)
        if r.status_code == 200:
            return r.json()

        # Raise exception if not 200
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Deletes an element
    ##
    @staticmethod
    def delete(model, elements, params=None):
        """Deletes data from model"""
        parameters = params if params is not None else {}
        ids = model.split(':')
        org = ids[0]
        project = ids[1]
        if len(ids) > 2:
            branch = ids[2]
        else:
            branch = 'main'

        opts = {
            'method': 'DELETE',
            'params': parameters,
            'body': elements
        }
        url = '/orgs/{}/projects/{}/branches/{}/elements'.format(org, project, branch)
        r = TriviumApi().make_request(url, **opts)
        if r.status_code == 200:
            return r.json()

        # Raise error if not 200
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))
