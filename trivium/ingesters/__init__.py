"""

Copyright 2021 Triple Dot Engineering LLC

"""
from .json_ingester import JSONIngester
from .yaml_ingester import YamlIngester

INGESTERS = [JSONIngester, YamlIngester]
