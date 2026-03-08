import unittest

from testproject.main import main


class SmokeTest(unittest.TestCase):
    def test_import(self) -> None:
        self.assertIsNotNone(main)
