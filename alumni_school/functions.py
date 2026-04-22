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
    return len(year) == 4 and year.isdigit()


def remove_text(year:str)->str:
    digits_list = re.findall("[0-9]", year)
    digits = ""
    for d in digits_list:
        digits = digits + d
    
    return digits

def has_DOB(year:str)-> str:
    match = re.search(r'\d+\/\d+/(\d+)', year)
    if match:
        return match.group(1)
    return None
    
def get_birth_year(year: str) -> str:
    if "Died:" in year:
        year = year.split("Died:")[0]
    dob_year = has_DOB(year)
    if dob_year:
        return add_digits(dob_year)
    two_digit = re.findall(r'[0-9][0-9]', year)
    if two_digit:
        return add_digits(two_digit[-1])
    years = re.findall(r'[0-9][0-9][0-9][0-9]', year)
    if years:
        return years[0]

    return ""



