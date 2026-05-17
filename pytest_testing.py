import pytest
from calc_test import sum

def test_sum():
    assert sum(2, 2) == 4
    assert sum(-6, 16) == 10
    assert sum(0, -1) == -1

def test2_sum():
    assert sum(2, 2) == 5