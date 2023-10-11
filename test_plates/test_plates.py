import plates


def test_symbols():
    assert plates.is_valid("!@#$%^&*()") == False
    assert plates.is_valid("wer!@4") == False
    assert plates.is_valid(" erjik") == False

def test_numbers():
    assert plates.is_valid("234567") == False
    assert plates.is_valid("x34567") == False
    assert plates.is_valid("xy3456") == True
    assert plates.is_valid("xyz456") == True
    assert plates.is_valid("xyza56") == True
    assert plates.is_valid("xyzab6") == True
    assert plates.is_valid("xy69uy") == False

def test_zero():
    assert plates.is_valid("h01234") == False
    assert plates.is_valid("gh0123") == False
    assert plates.is_valid("ghw012") == False
    assert plates.is_valid("ghwx01") == False
    assert plates.is_valid("eghwx0") == False

def test_length():
    assert plates.is_valid("w") == False
    assert plates.is_valid("wt") == True
    assert plates.is_valid("wts") == True
    assert plates.is_valid("wter") == True
    assert plates.is_valid("wttyu") == True
    assert plates.is_valid("wtqwef") == True
    assert plates.is_valid("wtqwefz") == False