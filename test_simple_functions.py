
import pytest

from simple_functions import *

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(1, -2) == -1
    assert add(1, 0.3) == 1.3

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False


def test_divide():
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5
    # vvv  Ne asteptam sa dea eroarea "ZeroDivisionError
    # assert divide(5, 0) == "ERROR"
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_to_positive():
    assert to_positive(0) == 0
    assert to_positive(-1) == 1
    assert to_positive(1) == 1
    assert to_positive(0) == 0
    with pytest.raises(TypeError):
        to_positive("50")






