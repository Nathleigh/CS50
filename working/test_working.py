import pytest
import working


def test_convert():
    assert working.convert("3:03 PM to 5:05 PM") == "15:03 to 17:05"
    assert working.convert("3 PM to 5 PM") == "15:00 to 17:00"
    assert working.convert("12 AM to 5 PM") == "00:00 to 17:00"

def test_hours_mins():
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:60 PM")
        working.convert("13:00 AM to 17:00 PM")

def test_no_spaces():
    with pytest.raises(ValueError):
        working.convert("3PM to 5PM")

def test_missing_to():
    with pytest.raises(ValueError):
        working.convert("3:03 PM 5:05 PM")
        working.convert("3 PM 5 PM")
        working.convert("3:03 PM - 5:05 PM")
        working.convert("3PM - 5PM")
