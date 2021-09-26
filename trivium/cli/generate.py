"""

Copyright 2021 Triple Dot Engineering LLC

"""
# pylint: skip-file
import docx
import json
from argparse import ArgumentParser
from ._subcommand_runner import SubcommandRunner
from .. import api


class Generate(SubcommandRunner):
    """The CLI generate command used to generate documents, reports, and more."""

    def __init__(self):
        super().__init__()
        self.program = 'trivium generate'
        self.description = 'This command can be used to generate things '
        self.description += '(documents, code, etc.) from your model.'


    def doc(self, _args):
        # pylint: disable=no-self-use
        """Generates a document"""
        print('Generating doc (not yet implemented) ...')
