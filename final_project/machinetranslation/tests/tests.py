import unittest
from .translator import englishToFrench, frenchToEnglish

class EnToFr(unittest.TestCase):
    def test_is_input_null(self):
        self.assertEqual(englishToFrench(''), None)
    
    def test_hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class FrToEn(unittest.TestCase):
    def test_is_input_null(self):
        self.assertEqual(frenchToEnglish(''), None)
    
    def test_hello(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
