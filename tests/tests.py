"""
Unit tests for Translation package
"""

import unittest

from translator import english_to_french, english_to_german

class TestEnFr(unittest.TestCase):
    """
    Test cases for English to French
    """

    def test_null(self):
        """
        If no input, return string stating as such.
        """
        self.assertEqual(english_to_french(""), "Lack of textual input.")

    def test_hello(self):
        """
        Test to see if it actually translates to French.
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_case_sensitivity(self):
        """
        Make sure mismatched casing doesn't ruin translation.
        """
        self.assertEqual(english_to_french("WoMaN"), "Femme")

    def test_numbers(self):
        """
        Make sure numbers are not present in the input.
        """
        self.assertEqual(english_to_french("Print hello 47 times"),
        "Please refrain from using numbers.")

class TestEnDe(unittest.TestCase):
    """
    Test cases for English to German
    """

    def test_null(self):
        """
        If no input, return string stating as such.
        """
        self.assertEqual(english_to_german(""), "Lack of textual input.")

    def test_hello(self):
        """
        Test to see if it actually translates to French.
        """
        self.assertEqual(english_to_german("Hello"), "Hallo")

    def test_case_sensitivity(self):
        """
        Make sure mismatched casing doesn't ruin translation.
        """
        self.assertEqual(english_to_german("WoMaN"), "Frau")

    def test_numbers(self):
        """
        Make sure numbers are not present in the input.
        """
        self.assertEqual(english_to_german("Print hello 47 times"),
        "Please refrain from using numbers.")


unittest.main()
