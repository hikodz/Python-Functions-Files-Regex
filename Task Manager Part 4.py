#Section 12: Python Functions, Files & Regex:
# Lesson Task Manager Part 7 ex 1:
strings = ['apple', 'banana', 'pear', 'orange'] 

def filter_strings(lst_string, char_return):
    lst_return = [string for string in lst_string if char_return in string]
    return lst_return

filtered_strings = filter_strings(strings, 'g')
print(filtered_strings)   # output: ["orange"]
##########################################################################
#Section 12: Python Functions, Files & Regex:
# Lesson Task Manager Part 7 ex 2:
numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1] 
def remove_duplicates(lst_number):
    dic_test = {}
    for num in lst_number:
        dic_test.setdefault(num)
    return list(dic_test.keys())

unique_numbers = remove_duplicates(numbers)
print(unique_numbers)     # output: [1, 2, 3, 4, 5]
##########################################################################
#Section 12: Python Functions, Files & Regex:
# Lesson Task Manager Part 7 ex 3:
# Original list of employees
employees = [
{'name': 'Mohamed Ali', 'age': 25, 'salary': 45_000,'department': 'Sales'},
{'name': 'Islam Ahmed', 'age': 30, 'salary': 60_000,'department': 'Marketing'},
{'name': 'Osama Ashraf', 'age': 35, 'salary': 38_000,'department': 'Sales'},
{'name': 'Seif Ali', 'age': 40, 'salary': 77_000,'department': 'Engineering'},
{'name': 'Ayman Hamed', 'age': 45, 'salary': 80_000,'department': 'Sales'},
{'name': 'Ahmed Ali', 'age': 33, 'salary': 76_000, 'department': 'Marketing'},
]
def give_raise(information, criteria, bonus):
    from copy import deepcopy
    new_information = deepcopy(information)
    for dic in new_information: 
        if dic['department']== criteria:
            dic['salary']+= bonus
    return new_information

def print_employees(information, new_information, criteria):
    for dic in information:
        if dic['department']== criteria:
            name = dic['name']
            previous_salary = dic['salary']
            new_salary = [dic_new['salary'] for dic_new in new_information if dic_new['name']==name]   
            print(f'{name} salary was {previous_salary}$ and is now {new_salary[0]}$')

# Give a raise of $10,000 to employees who meet the criteria of being in the Sales department
new_employees = give_raise(employees, 'Sales', 10_000)
# Print the new and old information of employees
print_employees(employees, new_employees, "Sales")
# Output:
# Mohamed Ali salary was 45,000.00$ and is now 55,000.00$
# Osama Ashraf salary was 38,000.00$ and is now 48,000.00$
# Ayman Hamed salary was 80,000.00$ and is now 90,000.00$
