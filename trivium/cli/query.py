"""

Copyright (c) 2021, Triple Dot Engineering LLC

"""

import json
from argparse import ArgumentParser
from ._subcommand_runner import SubcommandRunner
from .. import api
from .. import util
from ..logger import get_logger

logger = get_logger()

class Query(SubcommandRunner):
    """Interface with model"""

    def __init__(self):
        super().__init__()
        self.program = 'trivium query'
        self.description = 'Query a model'

    ##
    # Query the model for elements. Optional filters can br provided to
    # filter the results. The filters align to the TD Graph API query filters.
    ##
    def __run__(self, _args):
        parser = ArgumentParser(prog=f'{self.program} query')
        parser.add_argument(
            'model',
            metavar='org:proj[:branch]',
            type=str,
            help="model identifier in the form <orgId>:<projectId>"
        )
        parser.add_argument('--filter', '-f', default=[], nargs='*')
        parser.add_argument('--format', default='dataframe', choices=['table', 'dataframe', 'json'])
        args, unknown = parser.parse_known_args(_args)
        logger.debug('Unknown args: {}'.format(unknown))

        # convert the filters into query params
        params = {}
        for f in args.filter:
            key, val = f.split('=')
            params[key] = val

        # <ake api call
        elements = api.element.get(args.model, params=params)

        if args.format == 'json':
            print(json.dumps(elements, indent=4))
        # For tables and dataframes
        elif args.format == 'dataframe':
            # Convert elements array to data frame
            df = util.to_dataframe(elements)
            # Columns to display
            cols = ['id', 'name', 'type', 'documentation']
            for col in df.columns:
                if col.startswith('custom') and len(col.split('.')) <= 2:
                    cols.append(col)
            # Display data frame
            print(df[cols])
        elif args.format == 'table':
            api.RestElement.print_table([ util.flatten(e) for e in elements ])

        return 0
