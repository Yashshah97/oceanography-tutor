"""Smoke tests for tracker."""
import unittest

from oceanography_tutor import tracker


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tracker, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tracker) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
