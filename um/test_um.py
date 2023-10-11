import pytest
import um


def test_actual():
    assert um.count("um") == 1
    assert um.count("Good, um, morning") == 1
    assert um.count("Some yummy cake") == 0
    assert um.count("yummy") == 0
    assert um.count("Humpty Dumpty") == 0

def test_caps():
    assert um.count("Um, hello") == 1
