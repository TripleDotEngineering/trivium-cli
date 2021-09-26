"""

Copyright 2021 Triple Dot Engineering LLC

"""

import json
from .. import logger
from .. import api

class TriviumEgester:
    """
    The Trivium Egester takes model data and uploads it to a Trivium model.
    """

    name = 'trivium'

    def __init__(self, args):
        """Initializes the egester"""
        self.logger = logger.get_logger()

        # Validate the input
        assert isinstance(args.out_tgt, str)
        assert 2<= len(args.out_tgt.split(':')) <= 3

        # The model to post to
        self._target = args.out_tgt
        self._root = args.root if args.root is not None else 'model'

    def run(self, data):
        """Runs the egester"""
        for element in data:
            if element['parent'] is None:
                element['parent'] = self._root

            # Remove the contains field, it's not valid to send it to the API
            element.pop('contains', None)

        # Log some information about the amount of data being posted
        num = len(data)
        size = len(json.dumps(data)) / 1024
        unit = 'KB'
        if size > 1024*512:
            size = size / 1024
            unit = 'MB'
        self.logger.info(f'Posting {num} elements ({size} {unit})')

        response = api.element.put(self._target, data)
        print(response)
        return 0
