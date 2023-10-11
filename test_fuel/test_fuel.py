import fuel
import pytest

def test_full():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

def test_empty():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"

def test_nums():
    assert fuel.gauge(2) == "2%"
    assert fuel.gauge(22) == "22%"
    assert fuel.gauge(55) == "55%"
    assert fuel.gauge(98) == "98%"

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("0/4") == 0

def test_errors():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
        fuel.convert("5/4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")