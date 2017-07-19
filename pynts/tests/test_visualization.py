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

from pynts.visualization import plot_comparison


class VisualizationTest(unittest.TestCase):

    @log_capture()
    def test_emptysets(self, l):
        """Test pynts visualization with empty set"""
        ts, d1, d2 = [], numpy.array([]), numpy.array([])
        plot_comparison(timestamp_list=ts, data1=d1, data2=d2)
        l.check(
            ('pynts.visualization', 'ERROR', "Nothing to plot 'None', 'data1', 'data2'"),
        )

    @log_capture()
    def test_nansets(self, l):
        """Test pynts visualization with all NaNs mask"""
        ts, d1, d2 = [datetime(2000, 1, 1), datetime(2000, 1, 2)], numpy.array([1.0, numpy.NaN]), numpy.array([numpy.NaN, 2.0])
        plot_comparison(timestamp_list=ts, data1=d1, data2=d2)
        l.check(
            ('pynts.visualization', 'ERROR', "Nothing to plot 'None', 'data1', 'data2'"),
        )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
