from unittest import TestCase
from checker import Checker

class TestChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = Checker()

    def test_length_same(self):
        self.checker.update_length_similarity("123", "123")
        self.assertEqual(self.checker.get_length_similarity(), 60)
        pass

