"""
Unit Tests for Task 3: Password Pattern Validation
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from password_validator import validate_passphrase_comprehensive, is_mirrored_palindrome

class TestPasswordPatternValidation(unittest.TestCase):
    def test_valid_passphrases(self):
        valid = [
            "[Pass{Word(2026)}!]", "{Admin(1234)}[Secure]",
            "(Correct-Horse-Battery)", "C.ManojReddy{RA2411026050038}",
            "SimpleSecurePassphrase123"
        ]
        for p in valid:
            with self.subTest(p=p):
                self.assertTrue(validate_passphrase_comprehensive(p))

    def test_mismatched_brackets(self):
        invalid = ["([Password)]", "{UnclosedPassword2026", "Pass(word]]"]
        for p in invalid:
            with self.subTest(p=p):
                self.assertFalse(validate_passphrase_comprehensive(p))

    def test_mirrored_palindromes(self):
        mirrored = ["abba-abba", "passwordsdrowssap", "abc-X-cba"]
        for p in mirrored:
            with self.subTest(p=p):
                self.assertTrue(is_mirrored_palindrome(p))
                self.assertFalse(validate_passphrase_comprehensive(p))

if __name__ == "__main__":
    unittest.main()
