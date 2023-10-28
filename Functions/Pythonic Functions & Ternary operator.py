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
#####################################################################################
#Section 12: Python Functions, Files & Regex : 
# Lesson 7 - Pythonic Functions & Ternary operator file 2 : exersice 1  : 
# Complete this code to make special_sum function using kwargs (keyword arguments):
def special_sum(numbers, **kwargs):
    print(kwargs) # this code is a hint to see what is inside kwargs
    if kwargs.get("only_even") or kwargs.get("only_odd") :
        return sum([number for number in numbers if number % 2 == 0])
    elif kwargs.get("only_odd"):
        return sum([number for number in numbers if number % 2 != 0])
    elif kwargs.get("only_positive"):
        return sum([number for number in numbers if number > 0])
    elif kwargs.get("only_negative"):
        return sum([number for number in numbers if number < 0])
    elif kwargs.get("only_positive_even"):
        return sum([number for number in numbers if number % 2 == 0 and number > 0])
    elif kwargs.get("only_positive_odd"):
        return sum([number for number in numbers if number % 2 != 0 and number > 0])
    elif kwargs.get("only_negative_even"):
        return sum([number for number in numbers if number % 2 == 0 and number < 0])
    elif kwargs.get("only_negative_odd"):
        return sum([number for number in numbers if number % 2 != 0 and number < 0])
    return sum(numbers)

numbers = [1, -2, -3, 4, -5, -6, -7, 8, 9, -10, 11, 12, 13, 14, -15, -16, 17, 18, 19, 20]
print(f"Sum of all numbers: {special_sum(numbers)}")
print(f"Total even numbers: {special_sum(numbers, only_even=True)}")
print(f"Total odd numbers: {special_sum(numbers, only_odd=True)}")
print(f"Total positive numbers: {special_sum(numbers,only_positive=True)}")
print(f"Total negative numbers: {special_sum(numbers,only_negative=True)}")
print(f"Total positive even numbers: {special_sum(numbers,only_positive_even=True)}")
print(f"Total positive odd numbers: {special_sum(numbers,only_positive_odd=True)}")
print(f"Total negative even numbers: {special_sum(numbers,only_negative_even=True)}")
print(f"Total negative odd numbers: {special_sum(numbers,only_negative_odd=True)}")
#####################################################################################
# Lesson 7 - Pythonic Functions & Ternary operator file 2 : exersice 2  : 
# Complete this code to make print_grades function that take student name
# and his grades like the following:
def print_grades(name, **kwargs): 
    print(f'{name.title()} is grades:\n{"-"*20}')
    for sub, grade in kwargs.items():
        print(f'{sub:10}: {grade}')

print_grades("Mohamed Hamed", math=90, english=80, arabic=100, physics=95, chemistry=85)
print_grades("Ahmed Khaled", math=80, english=70, arabic=90, physics=85, chemistry=75)

#####################################################################################
# Lesson 7 - Pythonic Functions & Ternary operator file 2 : exersice 3  : 
# Make a function that generate a random password with the following requirements:
from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from random import choice, shuffle, sample
def randomPassword(lenght=8, complex=False):
    passwordUser = []
    if lenght < 8:
        print('The number of password content will be very low')
        lenght = 8
    if complex :
        passwordUser.extend(sample(punctuation, (lenght//2)+(lenght%2)))
        while len(passwordUser) < lenght :
            passwordUser.extend([choice(ascii_lowercase), choice(ascii_uppercase), choice(digits)])
    elif complex == False :
        while len(passwordUser) < lenght:
            passwordUser.extend([choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice(punctuation)])
    if len(passwordUser)>lenght:
        del passwordUser[(lenght-len(passwordUser)):]
    shuffle(passwordUser)
    passwordUser = ''.join(passwordUser)
    return f'your password is: {passwordUser}'
print(randomPassword(30, complex=True))
