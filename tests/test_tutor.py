"""Smoke tests for tutor."""
import unittest

from oceanography_tutor import tutor


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tutor, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tutor) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
