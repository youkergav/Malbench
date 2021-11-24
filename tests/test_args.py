import os
import unittest
import malbench.args as args

class TestArgs(unittest.TestCase):
    def setUp(self):
        self.folderpath = "tests/data/samples/"

    def test_args(self):
        # Test filepath
        results = args.Args([self.folderpath + "calc.exe"])
        self.assertListEqual(results.path, [os.path.abspath("tests/data/samples/calc.exe")])

        # Test folderpath
        results = args.Args([self.folderpath])
        test = [
            os.path.abspath("tests/data/samples/calc.exe"),
            os.path.abspath("tests/data/samples/notepad.exe"),
        ]
        self.assertListEqual(results.path, test)

        # Test verbose flag
        results = args.Args([self.folderpath + "calc.exe", "--verbose"])
        self.assertTrue(results.verbose)

        # Test no-banner flag
        results = args.Args([self.folderpath + "calc.exe", "--no-banner"])
        self.assertTrue(results.no_banner)

        # Test no arguments
        with self.assertRaises(SystemExit) as results:
            args.Args()
        self.assertEqual(results.exception.code, 2)

    def test_is_exectuable(self):
        self.assertTrue(args.Args.__is_executable__(self.folderpath + "calc.exe"))

    def test_get_path(self):
        # Test filepath
        self.assertListEqual(args.Args.__get_path__(self.folderpath + "calc.exe"), [os.path.abspath("tests/data/samples/calc.exe")])

        # Test folderpath
        test = [
            os.path.abspath("tests/data/samples/calc.exe"),
            os.path.abspath("tests/data/samples/notepad.exe"),
        ]

        self.assertListEqual(args.Args.__get_path__(self.folderpath), test)