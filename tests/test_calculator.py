from calculator.calculcator import add, div


def test_sum():
    assert add(1, 1) == 2


def test_div():
    assert div(4, 2) == 2
