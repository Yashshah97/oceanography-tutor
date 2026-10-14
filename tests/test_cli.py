import unittest
from oceanography_tutor import cli

class TestCLI(unittest.TestCase):

    def test_main_help(self):
        with self.assertRaises(SystemExit) as cm:
            cli.main(['-h'])
        self.assertEqual(cm.exception.code, 0)

    def test_main_version(self):
        with self.assertRaises(SystemExit) as cm:
            cli.main('--version')
        self.assertEqual(cm.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
