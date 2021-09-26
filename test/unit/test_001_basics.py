import unittest
from unittest.mock import MagicMock
from test.util import TriviumTestSuite, TriviumTest
import trivium


class TestBasics(TriviumTestSuite):

    # Returns True or False.
    @TriviumTest
    def test_Test_Framework(self):
        self.assertTrue(True)

    @TriviumTest
    def test_Util_Flatten(self):
        flat = trivium.util.flatten({
            'foo': 'bar',
            'custom': {
                'foo': 'bar',
                'baz': {
                    'qux': '???'
                }
            }
        })
        assert len(flat.keys()) == 3




if __name__ == '__main__':
    unittest.main()
