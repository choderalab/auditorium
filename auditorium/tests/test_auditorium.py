"""
Unit and regression test for the auditorium package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import auditorium


def test_auditorium_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "auditorium" in sys.modules
