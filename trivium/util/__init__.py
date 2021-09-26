#!/usr/bin/env python
"""
util/__init__.py

Copyright 2021 Triple Dot Engineering LLC

This file defines common utility functions and classes.
"""


import os
import collections
from pathlib import Path
import pandas as pd
from . import jmi
from ..config import VERSION


##
# Returns the Trivium CLI version as defined in the config.py file.
##
def get_version():
    """Returns the Trivium CLI version"""
    return VERSION


##
# Gets the Trivium Home directory. This is always a directory called ".trivium" in
# the user's home directory (as returned by Path.home()).
# If the .trivium directory does not exist, this function will create and
# initialized it.
##
def get_home():
    """Gets the Trivium home directory. If the home directory does not yet exist,
    it will be created and initialized.
    """
    home = str(Path.home())
    path = os.path.join(home, '.trivium')

    # If home doesn't exist, create it.
    if not os.path.isdir(path):
        os.makedirs(path)

        fname = os.path.join(path, 'config')
        with open(fname, 'w') as f:
            f.write('{}')

        fname = os.path.join(path, 'credentials')
        with open(fname, 'w') as f:
            f.write('{}')

    # Return the path to the home directory
    return path


def isfalsy(x):
    """Given an input returns True if the input is a "falsy" value. Where
    "falsy" is defined as None, '', or False."""
    return x is None or x == '' or x == False


def flatten(d, parent_key='', sep='.'):
    """
    Flattens a dictionary by making nesting fields dot (.) separated.
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def to_dataframe(elements):
    """
    Converts an array of elements to a dataframe
    """
    elements = [ flatten(e) for e in elements ]
    df = pd.DataFrame.from_dict(elements)
    return df


class Colors:
    """
    The colors util. This is a set of ASCII terminal color definitions for use
    in printed output.
    """
    GRAY = '\033[90m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
