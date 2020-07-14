import pytest

def func(x):
    return x+2

def test1():
    assert func(2) == 4

def test2():
    assert func(2) == 3