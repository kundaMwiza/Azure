# module to unit test functions in test_utils

# need pytest for testing
import pytest

# import functions to be tested
from .utils import *

# test function returns expected values
def test_add_ints():
    assert add_ints(5, 4) == 9

def test_divide_ints():
    # test divide by zero error
    with pytest.raises(ZeroDivisionError):
        divide_ints(5, 0)

    # test expected value
    assert divide_ints(3, 4) == 3 / 4
 