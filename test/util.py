#!/usr/bin/env python
################################################################################
#
# test/util.py
#
# Copyright (c) 2021, Triple Dot Engineering LLC
#
# Defines test utilities used across tests.
#
################################################################################

import trivium
import functools
import unittest
import os

colors = trivium.util.Colors

##
# An intermediate class used for common behavior in all tests
##
class TriviumTestSuite(unittest.TestCase):

    is_initiated = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


##
# A decorator to wrap tests. This is used for clean printing and
# formatting of test output.
##
def TriviumTest(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__.replace('test_', '', 1)
        name = name.replace('_', ' ')
        #name = name.title()
        name = '{}{}{}'.format(colors.BOLD, name, colors.ENDC)
        print('    {}'.format(name), end =' ')
        print('.'*(64 - len(name)), end=' ')

        # Call the test
        try:
            func(*args, **kwargs)

            ok = '{}OK{}'.format(colors.BOLD + colors.GREEN, colors.ENDC)
            print(ok)
        except AssertionError as e:
            fail = '{}FAIL{}'.format(colors.BOLD + colors.RED, colors.ENDC)
            print(fail, end=' ')
            print(e)
        except Exception as e:
            fail = '{}FAIL{}'.format(colors.BOLD + colors.RED, colors.ENDC)
            print(fail, end=' ')
            print(e)

        return func(*args, **kwargs)
    return wrapper


##
# Utility function to load a file from test resources as a string
##
def load_resource(s):
    __dirname = os.path.dirname(__file__)
    resources = os.path.join(__dirname, 'resources')
    jsonfile = os.path.join(resources, s)
    with open(jsonfile) as f:
        s = f.read()
    return s


##
# Utility function to count the number of elements in a JMI3 object.
##
def count_elements(ptr):
    ctr = 0
    for eid in ptr.keys():
        # Get the element and count it
        element = ptr[eid]
        ctr += 1

        # If the element has children, count them recursively
        contains = element['contains']
        if len(contains.keys()) > 0:
            ctr += count_elements(contains)
    return ctr
