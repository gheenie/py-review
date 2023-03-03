from src.setup import (setup)

def test_setup():
    assert setup() == 'hi world'
    