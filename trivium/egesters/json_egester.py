"""

Copyright 2021 Triple Dot Engineering LLC

"""

import json

class JSONEgester:
    """
    JSON Egester is used to output models as JSON.
    """

    name = 'json'

    def __init__(self, args):
        """Initializes the egester."""
        self._stdout = args.stdout

        if not self._stdout:
            self._target = args.out_tgt if args.out_tgt is not None else 'output.json'


    def run(self, data):
        """Runs the egester, given model data"""
        output = json.dumps(data, indent=4)
        if self._stdout:
            print(output)
        else:
            with open(self._target, 'w', encoding='utf-8') as f:
                f.write(output)
