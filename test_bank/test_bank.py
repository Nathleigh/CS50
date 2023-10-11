import bank

def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("hello123") == 0
    assert bank.value("hello 45ui") == 0
    assert bank.value("HELLO 45ui") == 0

def test_h():
    assert bank.value("hullo") == 20
    assert bank.value("h3llo") == 20
    assert bank.value("hi") == 20

def test_other():
    assert bank.value("good morning") == 100
    assert bank.value("1234") == 100
    assert bank.value("") == 100