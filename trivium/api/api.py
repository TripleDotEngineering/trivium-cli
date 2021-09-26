
#!/usr/bin/env python
"""
api/api.py

Copyright 2021 Triple Dot Engineering LLC

Defines the TriviumAPI class for interacting with the Triple Dot Graph API via
the command line or from Python.
"""
import json
import os
import requests
from .. import util


class TriviumApi:
    """
    The class for interacting with the Trivium/TripleDotGraph API
    """


    ##
    # Initializes the common information needed for an API call.
    ##
    def __init__(self,
        url='https://graph.triple.engineering/core',
        auth=(None,None)
    ):
        self._url = url
        self._auth = auth
        self._update_auth()


    ##
    # Updates the auth information based on the Trivium environment variables or
    # the credentials configuration. The environment variable take precedence.
    ##
    def _update_auth(self):
        """Updates the auth field from the environment variables or the
        credentials file."""

        _api_key_id = 'TRV_API_KEY_ID'
        _api_secret = 'TRV_API_SECRET'

        if util.isfalsy(self._auth[0]) and util.isfalsy(self._auth[1]):
            _username = os.environ.get(_api_key_id)
            _password = os.environ.get(_api_secret)
            self._auth = (_username, _password)

        if util.isfalsy(self._auth[0]) and util.isfalsy(self._auth[1]):
            home = util.get_home()
            credp = os.path.join(home, 'credentials')
            creds = json.loads(open(credp, 'r').read())
            if _api_key_id in creds.keys() and _api_secret in creds.keys():
                _username = creds[_api_key_id]
                _password = creds[_api_secret]
                self._auth = (_username, _password)


    ##
    # A wrapper function for all API requests. This sets the base URL and
    # sets up the auth header.
    ##
    def make_request(self, path, method='GET', params=None, body=None, dry_run=False):
        # pylint: disable=too-many-arguments
        """A request wrapper. This method makes the actual API call."""
        # Format params and URL
        parameters = params if params is not None else {}
        querystr = '&'.join(['{}={}'.format(k,v) for k,v in parameters.items()])
        url = '{}{}'.format(self._url, path)


        if dry_run:
            print('***** Dry-Run *****')
            print('{} {}?{}'.format(method, url, querystr))
            print(body)
            return None

        if body is not None:
            return requests.request(method, url, params=parameters, json=body, auth=self._auth)

        return requests.request(method, url, params=parameters, auth=self._auth)


    ##
    # Returns the status code returned by the test endpoint.
    ##
    def test(self):
        """Calls the test endpoint"""
        r = self.make_request('/test', method='GET')
        return r.status_code


    ##
    # Returns the JSON data returned by the version envpoint
    ##
    def version(self):
        """Calls the version endpoint"""
        r = self.make_request('/version', method='GET')
        if r.status_code == 200:
            return r.json()

        raise Exception('ApiError: {} {}'.format(r.status_code, r.text))
