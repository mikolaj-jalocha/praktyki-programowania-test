"""Exemplary calculator tests"""

import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    """tests"""
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """tests"""
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """tests"""
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected ", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """tests"""
    result = utils.divide(a, b)
    assert result == expected

import pytest
from utils import decimal_to_binary


@pytest.mark.parametrize("decimal, expected", [
    (0, "0b0"),
    (1, "0b1"),
    (10, "0b1010"),
    (100, "0b1100100"),
])
def test_decimal_to_binary_conversion(decimal, expected):
    """Test correct binary conversion."""
    assert decimal_to_binary(decimal) == expected


@pytest.mark.parametrize("decimal", [-1, 101])
def test_decimal_to_binary_out_of_range(decimal):
    """Test if out-of-range numbers raise an error."""
    with pytest.raises(ValueError):
        decimal_to_binary(decimal)


@pytest.mark.parametrize("decimal", [1.5, 2.7, -3.3])
def test_decimal_to_binary_non_integer(decimal):
    """Test if non-integer numbers raise an error."""
    with pytest.raises(ValueError):
        decimal_to_binary(decimal)