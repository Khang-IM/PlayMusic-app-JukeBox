import pytest
from library_item import LibraryItem

def test_initialization():
    item = LibraryItem("Song A", "Artist A", 3)
    assert item.name == "Song A"
    assert item.artist == "Artist A"
    assert item.rating == 3
    assert item.play_count == 0

def test_initialization_with_default_rating():
    item = LibraryItem("Song B", "Artist B")
    assert item.name == "Song B"
    assert item.artist == "Artist B"
    assert item.rating == 0
    assert item.play_count == 0

# Test the info method
def test_info():
    item = LibraryItem("Song A", "Artist A", 3)
    assert item.info() == "Song A - Artist A ***"

# Test the stars method
def test_stars():
    item = LibraryItem("Song A", "Artist A", 3)
    assert item.stars() == "***"

def test_stars_with_zero_rating():
    item = LibraryItem("Song B", "Artist B", 0)
    assert item.stars() == ""

def test_stars_with_full_rating():
    item = LibraryItem("Song C", "Artist C", 5)
    assert item.stars() == "*****"

# Test play count functionality
def test_play_count_initially_zero():
    item = LibraryItem("Song A", "Artist A", 3)
    assert item.play_count == 0

def test_increment_play_count():
    item = LibraryItem("Song A", "Artist A", 3)
    item.play_count += 1
    assert item.play_count == 1

# Test setting and getting rating
def test_set_rating():
    item = LibraryItem("Song A", "Artist A", 3)
    item.rating = 4
    assert item.rating == 4
