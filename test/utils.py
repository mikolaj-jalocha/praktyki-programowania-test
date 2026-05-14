"""Exemplary calculator functions"""
import string
from calendar import error


def add(a: int, b: int) -> int:
    """Function for adding values"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Function for substracting"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Function for multiplying"""
    return a * b


def divide(a: int, b: int) -> float:
    """Function for dividing."""
    return a / b

def decimal_to_binary(a: int) -> string:
    """Function for dividing."""
    if not isinstance(a, int) or a < 0 or a > 100:
        raise ValueError("Error happened")
    return bin(a)

