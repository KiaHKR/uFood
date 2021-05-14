"""Test OS validation."""


import unittest
import src.bin.validation as validation

class TestValidation(unittest.TestCase):
    """Test OS validation."""

    def test_checkOS(self):
        res = validation.checkOS("Windows")
        exp = None
        self.assertEqual(res, exp)
        with self.assertRaises(SystemExit):
            validation.checkOS("MacOS")