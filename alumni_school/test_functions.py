import pytest
from functions import *

def test_digits():
    assert add_digits("49") == '1949'

def test_four_digits():
    assert is_four_digits("1941") is True
 
def test_remove_text():
    assert remove_text("48 AD ASTR") == '48'
    
def test_has_DOB():
    assert has_DOB("DOB: 05/03/19") == '19'

def test_get_birth_year():
    assert get_birth_year("3/13/74") == "1974"
