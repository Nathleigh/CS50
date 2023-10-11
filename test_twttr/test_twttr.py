import twttr

def test_lower():
    assert twttr.shorten("1aeiou2") == "12"

def test_upper():
    assert twttr.shorten("1AEIOU2") == "12"

def test_punc():
    assert twttr.shorten(".,';:!@#$%^&*()") == ".,';:!@#$%^&*()"

def test_caps():
    assert twttr.shorten("rtghRTGH") == "rtghRTGH"
