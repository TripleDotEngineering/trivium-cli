#!/usr/bin/env python
"""
api/rest_user.py

Copyright 2021 Triple Dot Engineering LLC

Defines the RestUser class used to interact with users via the API.

"""
import json

from ._abc_rest_obj import RestObject
from .api import TriviumApi
from ..util import Colors


class RestUser(RestObject):
    """
    User-related object and methods for interacting with REST API
    """

    ##
    # RestUser constructor
    ##
    def __init__(self, data):
        super().__init__()
        self._data = data


    ##
    # Returns the string representation of a user
    ##
    def __repr__(self):
        return self.__str__()


    ##
    # Returns the the string representation of the user (as JSON)
    ##
    def __str__(self):
        return json.dumps(self._data, indent=4)


    ##
    # Takes a list of users as input and prints them in tabular format.
    ##
    @staticmethod
    def print_table(users):
        """Prints tablular users"""
        #fmt = '{username:12s} {email:32s} {lname:12s} {fname:12s} {preferredName:12s} {admin}'
        fmt = '{username:12s} {email:32s} {lname:12s} {fname:12s} {admin}'
        labels = {
            'username':     'Username',
            'email':        'E-Mail',
            'fname':        'First Name',
            'lname':        'Last Name',
            'preferredName':'Preferred Name',
            'admin':        'Is Admin?'
        }
        header_fmt = Colors.CYAN + Colors.BOLD
        print(header_fmt + fmt.format(**labels) + Colors.ENDC)

        for user in users:
            user_data = {}
            for key in user.keys():
                user_data[key] = user.get(key, '')
                if user_data[key] is None:
                    user_data[key] = ''
            print(fmt.format(**user_data))

    ##
    # Returns the current user
    ##
    @staticmethod
    def whoami():
        """Calls the whoami endpoint"""
        url = '/users/whoami'
        r = TriviumApi().make_request(url)

        if r.status_code == 200:
            return r.json()
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Gets a single user if user is specified, otherwise gets all users.
    ##
    @staticmethod
    def get(user=None):
        """Get a single user if user is provided, otherwise gets all users."""
        url = '/users' if user is None else '/users/{}'.format(user)
        r = TriviumApi().make_request(url)
        if r.status_code == 200:
            return r.json()

        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Posts one or more users based on input data.
    ##
    @staticmethod
    def post(data):
        """Creates one or mode users based on provided body data."""
        opts = {
            'method': 'POST',
            'params': {},
            'body': data
        }
        r = TriviumApi().make_request('/users', **opts)
        if r.status_code == 200:
            return r.json()

        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))


    ##
    # Deletes a user.
    ##
    @staticmethod
    def delete(username):
        """Creates one or mode users based on provided body data."""
        opts = {
            'method': 'DELETE',
            'params': {}
        }
        url = '/users/{0}'.format(username)
        r = TriviumApi().make_request(url, **opts)
        if r.status_code == 200:
            return r.json()
        raise Exception('TriviumApiError: {} {}'.format(r.status_code, r.text))
