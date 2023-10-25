from src.universal_hash_function.hash import Hash
from random import sample

def test_range():
    myhash = Hash(300)
    randlist = sample(range(0, pow(2, 16)), 600)

    for num in randlist:
        assert 0 <= myhash.hash(num) < 300

def test_integrity():
    myhash = Hash(300)
    randlist = sample(range(0, pow(2, 16)), 100)

    for num in randlist:
        call1 = myhash.hash(num)
        call2 = myhash.hash(num)
        assert call1 == call2

def test_uniqueness():
    myhash = Hash(5000)
    randlist = sample(range(0, pow(2, 16)), 100)

    randset = set(randlist)
    assert len(randset) == 100