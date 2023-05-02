from malbench.version import Version
from unittest import TestCase
from unittest.mock import patch


class TestVersion(TestCase):
    def test_version(self):
        result = Version.version()  # Run the disclaimer method.

        # Define expected results.
        with open("data/version.txt", "r") as f:
            expected = f.read()

        self.assertEqual(result, expected)  # Perform assertion.
