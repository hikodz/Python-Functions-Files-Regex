#Section 12: Python Functions, Files & Regex
# Lesson 5 - Function *args Project :
# Complete the following function to count the positive even numbers:
def count_positive_even_number(*args):
    return len([num for num in args if (num % 2 == 0 ) and (num > 0)])
count_positive_even = count_positive_even_number(1, 2, 3, -4, -5, -6, -7, 8, 9, 10)
print(count_positive_even)      # output : 3
###################################################################################
# Make a function that generates random even numbers allowing the user to
#  specify the number of even numbers to generate and the range of the numbers:
from random import randint
def generate_random_even_number(num_even_number=10, range_star=1, range_end=20):
    add = []
    while len(add) < num_even_number:
        num = randint(range_star, range_end)
        if num  % 2 == 0:
            add.append(num)
    return add
random_20_even_number = generate_random_even_number(20, 1, 100)
print(random_20_even_number)    # output : [الله اعلم]
###################################################################################
# Make a function that converts a list containing numbers as
#  string to a list containing numbers as integers:
def convert_list_to_integers(list_number):
    list_convert = [int(num) for num in list_number]
    return list_convert
numbers = convert_list_to_integers(["1", "2", "3", "4", "5"])
print(numbers)     # output : [1, 2, 3, 4, 5]

