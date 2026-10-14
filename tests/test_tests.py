'''Unit tests for Oceanography Flashcard Tutor tests'''

import unittest
from oceanography_tutor import tests

class TestTests(unittest.TestCase):

    def test_import(self):
        self.assertIsNotNone(tests)

if __name__ == '__main__':
    unittest.main(argv=[__file__])
