"""
Unittest for translation.py module
"""

import unittest
from translator import french_to_english, english_to_french

class TestMachineTranslation(unittest.TestCase):
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        self.assertIsNotNone(english_to_french(None))

    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
        self.assertIsNotNone(french_to_english(None))
        
#if __name__=='__main__':
#    unittest.main()