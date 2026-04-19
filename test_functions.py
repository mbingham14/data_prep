import pytest
from functions import *

def test_digits():
    assert add_digits("49") == '1949'

def test_four_digits():
    assert is_four_digits("1941") is True
 
def test_remove_text():
    assert remove_text("48 AD ASTR") == '48'
