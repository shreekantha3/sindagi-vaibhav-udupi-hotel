#!/usr/bin/env python3
"""Basic automated tests for generated site."""
import unittest
from pathlib import Path

class SiteTests(unittest.TestCase):
    def test_index_exists(self):
        self.assertTrue(Path("index.html").exists())

    def test_readme_exists(self):
        self.assertTrue(Path("README.md").exists())

if __name__ == "__main__":
    unittest.main()
