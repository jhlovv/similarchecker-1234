from unittest import TestCase
from checker import Checker

class TestChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = Checker()

    def test_length_same(self):
        self.checker.update_length_similarity("123", "123")
        self.checker.update_length_similarity("132", "123")
        self.assertEqual(self.checker.get_length_similarity(), 60)

    def test_length_0score(self):
        self.checker.update_length_similarity("A", "BB")
        self.assertEqual(self.checker.get_length_similarity(), 0)

