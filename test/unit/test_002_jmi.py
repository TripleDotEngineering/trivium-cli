import unittest
from unittest.mock import MagicMock
import json
import os

from test.util import load_resource, count_elements
from test.util import TriviumTestSuite, TriviumTest
import trivium

class TestJMIConversions(TriviumTestSuite):

    # Returns True or False.
    @TriviumTest
    def test_JMI_1_to_2_Conversion(self):
        # Load the model
        s = load_resource('sample_doc.json')
        model = json.loads(s)

        # Convert JMI 1 to 2 conversion
        converted = trivium.util.jmi.convert(model, 1, 2)

        # Verify conversion
        self.assertEqual(len(model), len(converted))
        for eid, element in converted.items():
            keys = element.keys()
            self.assertTrue('id' in keys)
            self.assertTrue('name' in keys)
            self.assertTrue('type' in keys)
            self.assertTrue('parent' in keys)
            self.assertTrue('contains' in keys)

    # Returns True or False.
    @TriviumTest
    def test_JMI_1_to_3_conversion(self):
        s = load_resource('sample_rand_sm.json')
        original = json.loads(s)
        model = json.loads(s)

        # Convert JMI 1 to 3 conversion
        jmi3 = trivium.util.jmi.convert(model, 1, 3)

        #print(json.dumps(jmi3, indent=4))
        N = count_elements(jmi3)
        self.assertEqual(len(model), N)


    # Returns True or False.
    @TriviumTest
    def test_JMI_3_to_1_conversion(self):
        # Load the JMI3 sample doc
        s = load_resource('sample_doc.jmi3.json')
        jmi3 = json.loads(s)
        n_elements = count_elements(jmi3)

        # Convert to JMI1
        jmi1 = trivium.util.jmi.convert(jmi3, 3, 1)

        # Validate the JMI1 object
        self.assertEqual(len(jmi1), n_elements)
        for element in jmi1:
            keys = element.keys()
            self.assertTrue('id' in keys)
            self.assertTrue('name' in keys)
            self.assertTrue('type' in keys)
            self.assertTrue('parent' in keys)
            self.assertTrue('contains' in keys)
            self.assertEqual(type(element['contains']), type([]))


if __name__ == '__main__':
    unittest.main()
