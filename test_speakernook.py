# test_speakernook.py
"""
Tests for SpeakerNook module.
"""

import unittest
from speakernook import SpeakerNook

class TestSpeakerNook(unittest.TestCase):
    """Test cases for SpeakerNook class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpeakerNook()
        self.assertIsInstance(instance, SpeakerNook)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpeakerNook()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
