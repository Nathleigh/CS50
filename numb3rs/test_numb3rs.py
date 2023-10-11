import pytest
import numb3rs


def test_validation():
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("255.255.255.255") == True

def test_invalid():
    assert numb3rs.validate("0.0.0") == False
    assert numb3rs.validate("cat") == False
    assert numb3rs.validate("0.0.0.299") == False


