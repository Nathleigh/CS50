import seasons
import pytest

def test_valid_date():
    assert seasons.get_dob("2022-8-1") == (2022, 8, 1)
    assert seasons.get_dob("2032-8-1") == (2032, 8, 1)
    assert seasons.get_dob("May 4, 1981") == None

