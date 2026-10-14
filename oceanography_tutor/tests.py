'''Unit tests for Oceanography Flashcard Tutor'''

import unittest
from io import StringIO
import sys

class TestTutor(unittest.TestCase):

    def test_tutorial(self):
        from oceanography_tutor import Tutor
        tutor = Tutor()
        self.assertEqual(tutor.get_next_question(), None)

    def test_answer(self):
        from oceanography_tutor import Tutor
        tutor = Tutor()
        with StringIO() as buf:
            sys.stdout = buf
            tutor.answer('tide', 'What is a tide?')
            sys.stdout = sys.__stdout__
            self.assertIn('Correct!', buf.getvalue())

    def test_progress(self):
        from oceanography_tutor import Tutor
        tutor = Tutor()
        self.assertEqual(tutor.get_progress(), 0)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
