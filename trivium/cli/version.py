#!/usr/bin/env python
"""

Copyright 2021 Triple Dot Engineering LLC

"""

from trivium.util import get_version
from trivium.cli._command import Command


class Version(Command):
    """The 'version' subcommand."""

    def __run__(self, args):
        # pylint: disable=unused-argument
        """Runs the command."""
        v = get_version()
        v = 'Trivium CLI v{}'.format(v)
        print(v)
        return 0
