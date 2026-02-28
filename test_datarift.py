# test_datarift.py
"""
Tests for DataRift module.
"""

import unittest
from datarift import DataRift

class TestDataRift(unittest.TestCase):
    """Test cases for DataRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataRift()
        self.assertIsInstance(instance, DataRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
