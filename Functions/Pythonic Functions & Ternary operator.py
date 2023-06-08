#Section 12: Python Functions, Files & Regex : 
# Lesson 7 - Pythonic Functions & Ternary operator : 
#* Make a function that sees if two numbers are divisible by 
#  each other or not with the default option to see if the 
#  number is divisible by 2 or not in 4 different ways.
#!----------------method number 1---------------------------------------------------------------
def is_div_by(number, divisor=1):
    if divisor == 1:
        if number %2==0:
            txt_messege = f'{number} is even'
        else:
            txt_messege = f'{number} is not even'
    else:
        if number % divisor ==0:
            txt_messege = f'{number} is divisible by {divisor}'
        else:
            txt_messege = f'{number} is not divisible by {divisor}'
    return txt_messege
print(is_div_by(5))
print(is_div_by(6))
print(is_div_by(5, 2))
print(is_div_by(5, 5))
#!----------------method number 2---------------------------------------------------------------
def is_div_by2(number, divisor=1):
    if divisor == 1:
        if number %2==0:
            return f'{number} is even'
        return f'{number} is not even'
    else:
        if number % divisor ==0:
            return f'{number} is divisible by {divisor}'
        return f'{number} is not divisible by {divisor}'
print(is_div_by2(5))
print(is_div_by2(6))
print(is_div_by2(5, 2))
print(is_div_by2(5, 5))
#!----------------method number 3---------------------------------------------------------------
def is_div_by3(number, divisor=1):
    if divisor == 1:
        return f'{number} is even' if number %2==0 else f'{number} is not even'
    else:
        return f'{number} is divisible by {divisor}' if number % divisor ==0 else f'{number} is not divisible by {divisor}'
print(is_div_by3(5))
print(is_div_by3(6))
print(is_div_by3(5, 2))
print(is_div_by3(5, 5))
#!----------------method number 4---------------------------------------------------------------
def is_div_by4(number, divisor=1):
    if divisor == 1:
        return f'{number} is even' if number %2==0 else f'{number} is not even'
    return f'{number} is divisible by {divisor}' if number % divisor ==0 else f'{number} is not divisible by {divisor}'
print(is_div_by4(5))
print(is_div_by4(6))
print(is_div_by4(5, 2))
print(is_div_by4(5, 5))


#Section 12: Python Functions, Files & Regex : 
# Lesson 7 - Pythonic Functions & Ternary operator file 1 : exersice 2  : 
def check_type_number(*number):
    
    return ["Even" if num %2==0 else "Odd" for num in number]
print(check_type_number(5))    # output:  ['Odd']
#############################################################################
#Lesson 7 - Pythonic Functions & Ternary operator file 1 : exersice 3 : 
def is_prime(number):
    check_prime = 2
    if (number ==1) or (number ==2):
        return "Prime"
    while check_prime < number:
        if number % check_prime ==0:
            return "Not Prime"
        check_prime += 1
    return "Prime"


print(is_prime(10))  # output: Not Prime
print(is_prime(11))  # output: Prime
print(is_prime(12))  # output: Not Prime
print(is_prime(13))  # output: Prime
#############################################################################
#Lesson 7 - Pythonic Functions & Ternary operator file 1 : exersice 4 : 
def convert_unit(number, unit):
    # convert unit basic math:
    convert_to_miles = number * 0.6214
    convert_to_km = number / 0.6214
    # convert unit for google :
    convert_to_F = (number * 9/5) + 32
    convert_to_C = (number - 32) * 5/9 
#---------------------------------------------
    if (unit.lower() == "miles") or (unit.lower() == "km"):
        return f'{number} Km is {convert_to_miles:.2f} Miles' if (unit.lower() == "km") else f'{number} Miles is {convert_to_km:.2f} Km'
    
    return f'{number} Celsius is {convert_to_F:.2f} Farhrenheit' if unit.lower()== 'celsius' else f'{number} Farhrenheit is {convert_to_C:.2f} Celsiust'
print(convert_unit(100, "Km"))         # output: 100 Km is 62.14 Miles
print(convert_unit(100, "Miles"))      # output: 100 Miles is 160.93 Km
print(convert_unit(30, "Celsius"))     # output: 30 Celsius is 86.00 Farhrenheit
print(convert_unit(86, "Farhrenheit")) # output: 86 Farhrenheit is 30.00 Celsiust
