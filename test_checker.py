from unittest import TestCase
from checker import Checker

class TestChecker(TestCase):
    def test_length_same(self):
        checker = Checker()
        checker.update_length_similarity("123", "123")
        self.assertEqual(checker.get_length_similarity(), 60)
        pass
