"""

Copyright 2021 Triple Dot Engineering LLC

"""
import argparse
import json
import time

from ..egesters import EGESTERS
from ..ingesters import INGESTERS
from .. import logger
from ._command import Command

logger = logger.get_logger()


class TransformCommand(Command):
    # pylint: disable=too-many-locals
    """
    Tranforms data from one input to an output format.
    """

    def __run__(self, _args):

        # Dynamically load ingesters and egesters
        ingesters = INGESTERS
        egesters = EGESTERS

        # Define the ingesters name to class mappings
        sources = {}
        for i in ingesters:
            sources[i.name] = i

        # Define the egesters name to class mappings
        targets = {}
        for i in egesters:
            targets[i.name] = i

        # Define valid source and target names
        valid_sources = list(sources.keys())
        valid_targets = list(targets.keys())

        # CLI parser
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--in',
            type=str,
            required=True,
            choices=valid_sources,
            help='the source format or type'
        )
        parser.add_argument(
            '--out',
            type=str,
            required=True,
            choices=valid_targets,
            help='the output format or type')
        parser.add_argument('--in-src', metavar='source', type=str, help='the input source')
        parser.add_argument('--out-tgt', metavar='target', type=str, help='the output target')
        parser.add_argument(
            '--stdout',
            action='store_true',
            help='tells the supported egesters to print to stdout'
        )
        parser.add_argument(
            '--root',
            type=str,
            help='Sets the root element for applicable egesters'
        )
        args, unknown = parser.parse_known_args(_args)

        # Output args for debug
        logger.debug(args)
        logger.debug(unknown)

        # Keep track of start time
        start = time.time()
        logger.info('Initializing ...')

        # Initialize the ingester and egester
        ingester_name = getattr(args, 'in') # Needed because "in" is a python keyword
        logger.verbose('Initializing ingester: {} ...'.format(ingester_name))
        ingester = sources[ingester_name](args)
        logger.verbose('Ingester initialized.')

        # Initialize the egester
        egester_name = args.out
        logger.verbose('Initializing egester: {} ...'.format(egester_name))
        egester = targets[egester_name](args)
        logger.verbose('Egester initialized.')

        # Run the ingester
        logger.info('Running ingester ...')
        model = ingester.run()

        # Run the egester
        logger.info('Running egester ...')
        egester.run(model)

        # Do wrap-up
        elapsed = time.time() - start
        self.wrapup(model, elapsed)
        return 0


    def wrapup(self, model, elapsed):
        # pylint: disable=no-self-use
        """Finishes and logs the transformation results."""
        logger.info('Wrapping up ...')

        # Get the number of model elements
        n_elements = len(model)

        # Get the model size
        size = len(json.dumps(model, indent=4)) / 1024
        unit = 'KB'

        if size > 1024*512:
            size = size / 1024
            unit = 'MB'

        fmt = 'Complete. Processed model with {} elements ({:.2f} {}) in {:.3f} seconds.'
        logger.info(fmt.format(n_elements, size, unit, elapsed))
