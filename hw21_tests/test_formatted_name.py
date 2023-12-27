import pytest

from hw21_tests.formatted_name import formatted_name


def test_formatted_name_with_middle_name():
    assert formatted_name("john", "doe", "middle") == "John Middle Doe"

def test_formatted_name_without_middle_name():
    assert formatted_name("pamela", "smith") == "Pamela Smith"

def test_formatted_name_with_empty_spaces():
    assert formatted_name("", "doe") == " Doe"
    assert formatted_name("john", "") == "John "
    assert formatted_name("", "") == " "


