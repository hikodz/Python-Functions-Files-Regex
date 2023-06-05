#Section 12: Python Functions, Files & Regex
# Lesson 4 - Return & Scopes Project :
#  exercise 1 : Make a function that sums only the odd numbers in a list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sum_odd_numbers_user(numbers_user):
    
    total = 0
    for num in numbers_user:
        if num % 2 != 0: 
            total += num 
    return total
total_odd = sum_odd_numbers_user(numbers)
print(total_odd)     # output 25

# exercise 2 :Make a function that returns the maximum even number in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def maximum_even_number(list_user):
    maximum_even = list_user[0]
    for num in list_user:
        if num % 2 == 0 and num > maximum_even:
            maximum_even = num 
    return maximum_even    # output 8

# exercise 3 :Make a function that returns the minimum odd number in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def minimum_odd_number(list_user):
    minimum_odd = list_user[0]
    for num in list_user:
        if num % 2 != 0 and num < minimum_odd:
            minimum_odd = num 
    return minimum_odd # output 1

# exercise 4 :Make a function that returns the enumeration of even numbers in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def enumeration_even_number(list_user):
    enumeration  = 0
    for num in list_user:
        if num % 2 == 0 :
            enumeration += 1
    return enumeration   # output 4

# exercise 5 :Make a function that returns the number of negative odd numbers in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def enumeration_odd_negative(list_user):
    enumeration  = 0
    for num in list_user:
        if num % 2 != 0 and num < 0:
            enumeration  += 1
    return enumeration    # output 0
# exercise 6 :Make a function that returns the string while making vowels and the first letter of each word capital:
txt = "welcome at codezilla python course we are happy to have you here"
def convert_txt(txt_user):
    vowels = ["a", "e", "i", "o", "u"]
    convert_result = txt_user.title()
    for vowel in vowels:
        convert_result = convert_result.replace(vowel, vowel.capitalize())
    return convert_result 
    #output : WElcOmE At COdEzIllA PythOn COUrsE WE ArE HAppy TO HAvE YOU HErE