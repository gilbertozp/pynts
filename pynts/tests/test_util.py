"""
Basic tests for pynts.visualization

N.B.: MacOSX matplotlib backend on virtualenv requires extra configs,
      possibly using virtualenv/bin/frameworkpython solution;
      if this is the case, use:
          (env)$ frameworkpython -m pytest -v
      instead of the regular:
          (env)$ pytest -v

@author: Gilberto Pastorello
@contact: gzpastorello@lbl.gov
@date: 2017-07-17
"""
import unittest
import numpy

from datetime import datetime
from testfixtures import log_capture

from pynts import PyntsError
from pynts.util import extract_columns, extract_interval

class UtilTest(unittest.TestCase):

    def setUp(self):
        self.data = numpy.zeros(10, dtype=[('ts', 'a25'), ('a', 'f8'), ('b', 'f8')])

    @log_capture()
    def test_timestamp_not_found(self, l):
        """Test pynts extract columns with timestamp column parameter not found"""
        extract_columns(data=self.data, columns=['a'], timestamps=['timestamp'])
        l.check(
            ('pynts.util', 'WARNING', "Couldn't find timestamps '['timestamp']' in data, using 'ts' instead"),
        )

    def test_no_timestamp(self):
        """Test pynts extract columns with no timestamp column available"""
        self.assertRaises(PyntsError, extract_columns, self.data[['a', 'b']], ['a'], ['timestamp'])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
