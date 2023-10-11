import jar
import pytest

j = jar.Jar()

def test_init():
    assert j.capacity == 12
    j2 = jar.Jar(5)
    assert j2.capacity == 5

def test_add():
    assert j.size == 0
    assert str(j) == ""
    j.deposit(6)
    assert j.size == 6
    assert str(j) == "🍪🍪🍪🍪🍪🍪"

def test_remove():
    j.withdraw(1)
    assert j.size == 5
    assert str(j) == "🍪🍪🍪🍪🍪"

def test_errors():
    with pytest.raises(ValueError):
        j.deposit(999)
        j.deposit(99)
        j.withdraw(999)