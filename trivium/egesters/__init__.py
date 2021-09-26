"""

Copyright 2021 Triple Dot Engineering LLC

"""
from .json_egester import JSONEgester
from .yaml_egester import YamlEgester
from .api_egester import TriviumEgester

EGESTERS = [JSONEgester, YamlEgester, TriviumEgester]
