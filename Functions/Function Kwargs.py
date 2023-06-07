#Section 12: Python Functions, Files & Regex
# Lesson 5 - Function *args Project :
#Make a special sum function that can sum all numbers, only even numbers,
#  only odd numbers, only positive numbers, and only negative numbers:
number_test = [1, 2, 3, -4, -5, -6, -7, 8, 9, 10]

def sum_special(numbers, only_even=False, only_odd=False, olny_positive=False, only_negative=False):
    total = 0
    for num in numbers:
        if only_even :
            if num %2==0:
                total+=num
        elif only_odd:
            if num % 2!=0:
                total+=num
        elif olny_positive:
            if num > 0 :
                total+=num
        elif only_negative:
            if num <0:
                total+=num
        else:
            total+=num
    return total

print(sum_special(number_test))                     #output : 11
print(sum_special(number_test, only_even=True))     #output : 10
print(sum_special(number_test, only_odd=True))      #output : 1
print(sum_special(number_test, olny_positive=True)) #output : 33
print(sum_special(number_test, only_negative=True)) #output : -22

###################################################################################
# Make a function that converts a list containing numbers as string or float to a list
#  containing numbers as integers with an option to convert to float and an option to convert to string:
str_lst = ["1.5", "2", "3.5", "4", "5"]
float_lst = [1.5, 2.5, 3.5, 4.5, 5.5]
def convert_list_to_integers(lst_number, convert_to_string=False, convert_to_float=False):
    lst_result = []
    for num in lst_number:
        if convert_to_float:
            lst_result.append(float(num))
        elif convert_to_string:
            lst_result.append(str(num))
        else:
            lst_result.append(int(float(num)))
    return lst_result
print(convert_list_to_integers(str_lst))                            #output : 1, 2, 3, 4, 5]
print(convert_list_to_integers(str_lst, convert_to_float=True))     #output : [1.5, 2.0, 3.5, 4.0, 5.0]
print(convert_list_to_integers(float_lst, convert_to_string=True))  #output : ['1.5', '2.5', '3.5', '4.5', '5.5']
###################################################################################
# Make a function that the maximum even number from a list of arguments allowing 
# the user to get, if he chooses, the second maximum even number till the nth maximum even number:
def max_even_number(*args, nth_max_even_number=1):
    lst_even_num = [num for num in args if num % 2==0]
    lst_even_num.sort(reverse=True)
    return lst_even_num[nth_max_even_number-1]
print(max_even_number(1, 2, 3, -4, -5, -6, -7, 8, 9, 10))                        #output : 10
print(max_even_number(1, 2, 3, -4, -5, -6, -7, 8, 9, 10, nth_max_even_number=3)) #output : 2

###################################################################################
# Make a function that calculates the average of a list of arguments allowing the user
#  to pass a list of numbers as a single argument or pass a list of numbers as multiple arguments:
def average(*args):
    if len(args) == 1:
        return sum(args[0]) / len(args[0])
    else:
        return sum(args) / len(args)
    
print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))   #output : 5.0
print(average([1, 2, 3, 4, 5, 6, 7, 8, 9])) #output : 5.0
print(average((1, 2, 3, 4, 5, 6, 7, 8, 9))) #output : 5.0
print(average({1, 2, 3, 4, 5, 6, 7, 8, 9})) #output : 5.0