import pytest


@pytest.mark.parametrize("x, y, expected", [(4, 7, 11)])
def test_addition(x, y, expected):
    total = x + y
    assert total == expected
