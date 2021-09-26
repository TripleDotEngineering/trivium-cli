"""

Copyright 2021 Triple Dot Engineering LLC

"""

import json

class JSONIngester:
    """
    Ingests a model from a JSON file containing an array of elements (JMI Type 1)
    """

    name = 'json'


    def __init__(self, args):
        """Initializes the ingester"""
        self.file = args.in_src


    def run(self):
        """Runs the ingester"""
        with open(self.file) as f:
            model = json.loads(f.read())
        return model
