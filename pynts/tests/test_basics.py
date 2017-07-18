"""
Basic tests for pynts

@author: Gilberto Pastorello
@contact: gzpastorello@lbl.gov
@date: 2017-07-17
"""
import unittest

import pynts

class BasicTest(unittest.TestCase):

    def test_version(self):
        """Test pynts module has '__version__' attribute"""
        self.assertTrue(hasattr(pynts, '__version__'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
