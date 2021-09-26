"""

Copyright 2021 Triple Dot Engineering LLC

"""
import yaml
from ..util import jmi

class YamlIngester:
    """
    Ingests a model from a YAML file
    """

    name = 'yaml'

    def __init__(self, args):
        """Initializes the ingester"""
        self.file = args.in_src


    def run(self):
        """Runs the ingester"""
        with open(self.file) as f:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(f, Loader=yaml.FullLoader)

        jmi3 = data['Model']
        model = jmi.convert(jmi3, 3, 1)
        return model
