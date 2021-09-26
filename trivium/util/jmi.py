#!/usr/bin/env python
"""
jmi.py

Copyright 2021 Triple Dot Engineering LLC

This file provides functions for converting between JMI format types.
JMI, or JSON Model Interchange, is a format for exchanging model data.
"""

import json


def convert(model, intype, outtype):
    """
    Takes in a model, an input JMI type (1, 2, or 3), and an output JMI type.
    Calls the appropriate conversion function and returns the converted object.
    """
    if intype == 1 and outtype == 2:
        return _convert12(model)
    elif intype == 1 and outtype == 3:
        return _convert13(model)
    elif intype == 2 and outtype == 3:
        return _convert23(model)
    elif intype == 2 and outtype == 1:
        raise Exception('JMI 2 to 1 conversion is not yet supported.')
    elif intype == 3 and outtype == 2:
        raise Exception('JMI 3 to 2 conversion is not yet supported.')
    elif intype == 3 and outtype == 1:
        return _convert31(model)
    else:
        raise Exception('Unsupported JMI conversion.')


def _convert12(model):
    """
    Converts a model from JMI type 1 to JMI type 2.
    """
    # Convert array to object
    results = {}
    for element in model:
        results[element['id']] = element

        # Update contains field if needed
        if 'contains' not in element.keys():
            element['contains'] = []
            for i in model:
                if i['parent'] == element['id']:
                    element['contains'].append(i['id'])
    return results



def _convert13(model):
    """
    Converts a model from JMI type 1 to JMI type 3.
    """
    jmi2 = _convert12(model)
    return _convert23(jmi2)


def _convert23(model):
    """
    Converts a model from JMI type 2 to JMI type 3.
    """
    # Create an array for elements with no children
    empty = []

    # Loop through each element
    for e in model.keys():
        element = model[e]

        # If the element has no children, add to empty
        if len(element['contains']) == 0:
            empty.append(element['id'])

        # Convert array of strings to object
        obj = {}
        for i in element['contains']:
            obj[i] = i

        # Set the contains equal to the object
        element['contains'] = obj

    # Call JMI 2->3 Helper
    model_ref = json.loads(json.dumps(model))
    _jmi23_helper(model_ref, model, empty)

    # Return modified JMI2 object
    return model


def _jmi23_helper(model_ref, jmi2, ids):
    """
    A helper function to recursively convert from JMI type 2 to JMI type 3.
    """
    # Create array for lowest level elements
    empties = []

    # Loop through each id
    for i in ids:
        element = model_ref[i]

        # Get the parent ID
        if isinstance(element['parent'], dict):
            parentID = element['parent']['id']
        else:
            parentID = element['parent']

        # If parent is none, nothing to do
        if parentID is None:
            continue

        # Otherwise set the parent
        parent = jmi2[parentID]

        # Move element to its parent's contains field
        # and remove the element from the JMI2 object
        parent['contains'][i] = element
        if i in jmi2.keys():
            del jmi2[i]

        # Get the ID of the parent's parent
        if (isinstance(parent['parent'], dict) and parent['parent'] is not None):
            parentsParent = jmi2[parent['parent']['id']]
        elif parent['parent'] is not None:
            parentsParent = jmi2[parent['parent']]
        else:
            parentsParent = None

        # If all of the items in contains are objects, the parent is lowest level
        is_lowest = True
        for k in parent['contains'].keys():
            el = parent['contains'][k]
            if isinstance(el, dict) and 'id' not in el.keys():
                is_lowest = False

        # If we're at the lowest level and there is a grandparent, we need to
        # process another layer, add the parent to the empties list.
        if is_lowest and parentsParent is not None:
            empties.append(parentID)


    # If there are still lowest level elements, recursively call function
    if len(empties) > 0:
        _jmi23_helper(model_ref, jmi2, empties)


def _convert31(pkg):
    """
    Converts from JMI type 3 to JMI type 1.
    """

    ##
    # A nested helper function to handle recursive JMI 3 to 1 conversion.
    ##
    def _jmi31_helper(element, element_id):
        # Reinsert the missing ID field
        element['id'] = element_id

        # Add the element to the results array
        results.append(element)

        if 'contains' in element.keys():
            # For each child element, recursively convert
            for key in element['contains'].keys():
                child = element['contains'][key]
                _jmi31_helper(child, key)
            # Update the element object to a list of contains IDs
            element['contains'] = list(element['contains'].keys())
        else:
            # If contains is not defined, update it to an empty list
            element['contains'] = []

    results = []
    for key in pkg.keys():
        element = pkg[key]
        _jmi31_helper(element, key)

    # An intermediate JMI 2 step for fast parent correction
    jmi2 = {}
    for i in results:
        jmi2[i['id']] = i

    # Do a final pass to correct parents
    for element in results:
        for child in element['contains']:
            c = child
            jmi2[c]['parent'] = element['id']
    # One more to fix the roots
    for element in results:
        if 'parent' not in element.keys():
            element['parent'] = None

    return results
