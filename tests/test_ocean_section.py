"""
Tests the ocean section class
"""
import sys
from pathlib import Path

# Add the source directory to the path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.ocean_section import Ocean_Section

def test_initialization():
    """
    Tests if the Ocean Section class can create an instance
    """
    test_section = Ocean_Section()
    assert test_section is not None
    assert isinstance(test_section, Ocean_Section)