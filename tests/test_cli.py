"""Smoke tests for cli."""
import unittest

from oceanography_tutor import cli


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(cli, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(cli) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
