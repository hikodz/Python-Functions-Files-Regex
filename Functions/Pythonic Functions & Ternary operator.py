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
