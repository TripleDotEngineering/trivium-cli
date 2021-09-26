#!/usr/bin/env python
"""

Copyright 2021 Triple Dot Engineering LLC

"""

import argparse
import json
import os
from getpass import getpass
from ._command import Command
from .. import util


class Configure(Command):
    """The configure command"""

    def __run__(self, args):
        """Runs the command."""
        parser = argparse.ArgumentParser(prog='trivium configure')
        parser.parse_known_args(args)

        # Get credentials
        api_key_id = input('Enter Trivium API Key ID: ')
        api_key_secret = getpass('Enter Trivium API Secret: ')
        creds = json.dumps({
            'TRV_API_KEY_ID': api_key_id,
            'TRV_API_SECRET': api_key_secret
        }, indent=4)

        # Store in creds file
        credp = os.path.join(util.get_home(), 'credentials')
        with open(credp, 'w') as f:
            f.write(creds)
        return 0
