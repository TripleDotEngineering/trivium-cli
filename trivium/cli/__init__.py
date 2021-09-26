"""

Copyright 2021 Triple Dot Engineering LLC

"""

import sys
from argparse import ArgumentParser


from . import generate
from . import version
from . import configure
from . import whoami
from . import query
from . import transform

from ..logger import TriviumLogger
logger = TriviumLogger.get_logger()



def main():
    """
    Runs the CLI
    """
    # Build the top-level command-line parser
    parser = ArgumentParser()
    parser.add_argument('subcommand', help='subcommand')
    parser.add_argument(
        '--log-level',
        choices=logger.get_levels(),
        help='set the log level to verbose'
    )
    args = parser.parse_args(sys.argv[1:2])
    args2, unknown = parser.parse_known_args(sys.argv[1:])

    # Set the log level
    if args2.log_level:
        logger.set_level(args2.log_level)

    logger.debug('Unknown commands: {}'.format(unknown))

    # These are the available commands
    commands = {
        'generate': generate.Generate,
        'version': version.Version,
        'configure': configure.Configure,
        'whoami': whoami.WhoAmI,
        'query': query.Query,
        'etl': transform.TransformCommand
    }

    cmd = commands.get(args.subcommand, None)

    # Error check - if unknown command, fail
    if cmd is None:
        print(f'Unknown command: {args.subcommand}')
        return 1

    # Run the command
    logger.debug(f'Running command: {args.subcommand}')
    return cmd().__run__(sys.argv[2:])
