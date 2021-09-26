#!/usr/bin/env python
"""

Copyright 2021 Triple Dot Engineering LLC

"""
import argparse
import json
from trivium.cli._command import Command
from .. import api


class WhoAmI(Command):
    """
    Queries the related Triple Dot Graph endpoint and
    returns the profile information for the current user.
    """

    def __run__(self, args):
        """Runs the command"""
        parser = argparse.ArgumentParser(prog='trivium whoami', description=WhoAmI.__doc__)
        parser.parse_known_args(args)

        user = api.user.whoami()
        print(json.dumps(user, indent=4))
        print('')
        return 0
