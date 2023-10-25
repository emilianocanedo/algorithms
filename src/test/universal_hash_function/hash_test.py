import pytest

from src.universal_hash_function.hash import Hash

def test_range():
    myhash = Hash(300)
    assert myhash.hash(6656504) < 300
    assert myhash.hash(4349854) < 300
    assert myhash.hash(543212) < 300