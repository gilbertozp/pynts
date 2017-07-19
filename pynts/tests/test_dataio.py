"""
Basic tests for pynts.dataio

@author: Gilberto Pastorello
@contact: gzpastorello@lbl.gov
@date: 2017-07-17
"""
import unittest
import numpy

from datetime import datetime
from testfixtures import log_capture

from pynts import PyntsError
from pynts.dataio import get_dtype, get_fill_value, get_timestamp_format_from_resolution


class DataIOTest(unittest.TestCase):

    def test_dtype(self):
        """Test data type retrieval based on variable label"""
        self.assertEqual(get_dtype(variable='TIMESTAMP'), 'a25')
        self.assertEqual(get_dtype(variable='timestamp'), 'a25')
        self.assertEqual(get_dtype(variable='other'), 'f8')
        self.assertEqual(get_dtype(variable='TS', strtest=['TS']), 'a25')
        self.assertEqual(get_dtype(variable='ts', strtest=['TS']), 'a25')

    def test_fill_value(self):
        """Test fill value retrieval based on data type"""
        self.assertEqual(get_fill_value(dtype='a25'), '')
        self.assertEqual(get_fill_value(dtype='i8'), -9999)
        self.assertTrue(numpy.isnan(get_fill_value(dtype='f8')))

    def test_timestamp_format(self):
        """Test timestamp format retrieval based on timestamp variable sample"""
        self.assertEqual(get_timestamp_format_from_resolution(sample="19991022113344"), "%Y%m%d%H%M%S")
        self.assertEqual(get_timestamp_format_from_resolution(sample="199910221133"), "%Y%m%d%H%M")
        self.assertEqual(get_timestamp_format_from_resolution(sample="1999102211"), "%Y%m%d%H")
        self.assertEqual(get_timestamp_format_from_resolution(sample="19991022"), "%Y%m%d")
        self.assertEqual(get_timestamp_format_from_resolution(sample="1999295"), "%Y%j")
        self.assertEqual(get_timestamp_format_from_resolution(sample="199910"), "%Y%m")
        self.assertEqual(get_timestamp_format_from_resolution(sample="1999"), "%Y")

        self.assertRaises(PyntsError, get_timestamp_format_from_resolution, "20")

        self.assertRaises(ValueError, get_timestamp_format_from_resolution, "200A")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
