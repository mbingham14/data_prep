import re

def add_digits(year:str)-> str:
    year = year.strip()
    if len(year) == 4:
        return year
    elif len(year) == 2:
        return "19" + year
    elif len(year) == 1:
        return "19" + "0" + year
    else:
        return "19" + year

def is_four_digits(year:str)-> bool:
    if re.search('[0-9][0-9][0-9][0-9]', year) is not None:
        return True
    else:
        return False

def remove_text(year:str)->str:
    digits_list = re.findall("[0-9]", year)
    digits = ""
    for d in digits_list:
        digits = digits + d
    
    return digits

    
'''
def has_question(year:str)-> int:

def dob_empty(year:str)-> int:

def has_signs(year:str)-> int:

def has_location(year:str)-> int:

def has_abt(year:str)-> int:
'''



