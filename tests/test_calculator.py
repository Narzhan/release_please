import pytest
from calculator.calculcator import add, div, subtract, modulo, multiply


def test_sum():
    assert add(1, 1) == 2


def test_div():
    assert div(4, 2) == 2


def test_sub():
    assert subtract(4, 4) == 0


def test_mod():
    assert modulo(4, 2) == 0


def test_multiply():
    assert multiply(2, 2) == 4


def test_biv_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert div(4, 0)
