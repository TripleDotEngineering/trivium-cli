"""

Copyright 2021 Triple Dot Engineering LLC

Defines the subcommand runner base class.

"""

import argparse
from .. import logger

logger = logger.get_logger()

class SubcommandRunner:
    """
    The SubcommandRunner base class is used for commands that have subcommands.
    The class automatically defines the subcommands based on the class methods
    defined on the inheriting class.
    """

    def __init__(self):
        self.program = 'trivium'
        self.description = 'This is the Trivium CLI'


    def __run__(self, _args):
        """Runs the subcommand."""
        parser = argparse.ArgumentParser(
            description=self.description,
            usage=f'{self.program} <command> [<args>]'
        )
        parser.add_argument('subcommand', help='Subcommand to run')
        args, unknown = parser.parse_known_args(_args[:1])
        logger.debug('Unknown commands: {}'.format(unknown))

        # Lookup command, if not found, print help and error
        if not hasattr(self, args.subcommand) or args.subcommand.startswith('_'):
            print('Unrecognized command')
            parser.print_help()
            return -1

        # If found, run the command
        getattr(self, args.subcommand)(_args[1:])
        return 0
