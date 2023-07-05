def average(*args):
    try:
        if len(args) ==1:
            return f"The average is: {int(sum(args[0]) / len(args[0]))}"
        return f"The average is: {int(sum(args) / len(args))}"
    except ZeroDivisionError:
        return "Please Enter Numbers to Calculate Average"
    except TypeError:
        return 'Cannot Enter a String'
    
print(average(1, 2, 3, 4, 5))
print(average([1, 2, 3, 4, 5]))
print(average((1, 2, 3, 4, 5)))
print(average({1, 2, 3, 4, 5}))
print(average([]))
print(average("Hello"))
print(average(1, 2, 3, 4, "5"))
print(average())

employees = [
{'name': 'Mohamed Ali', 'age': 25,'salary': 45_000, 'department': 'Sales'},
{'name': 'Islam Ahmed', 'age': 30,'salary': 60_000, 'department': 'Marketing'},
{'name': 'Osama Ashraf', 'age': 35, 'salary': 38_000, 'department': 'Sales'},
{'name': 'Seif Ali', 'age': 40,'salary': 77_000, 'department': 'Engineering'},
{'name': 'Ayman Hamed', 'age': 45, 'salary': 80_000, 'department': 'Sales'},
{'name': 'Ahmed Alaa', 'age': 33,'salary': 76_000, 'department': 'Marketing'}
]

def give_raise(information, criteria, bonus):
    from copy import deepcopy
    try:
        rank = [info['department']for info in information]
        if criteria not in rank :
            print("Please enter the employee's rank correctly")
            return
        if len(information)==0:
            print("Please enter the empoloyee information correctly")
            return
        new_information = deepcopy(information)
        for dic in new_information: 
            if dic['department']== criteria:
                dic['salary']+= bonus
        return new_information
    except TypeError:
        print("Please enter the bonus in the form of a valid number")

def print_employees(information, new_information, criteria):
    try:
        rank = [info['department']for info in information]
        if criteria not in rank :
            return "Please enter the employee's rank correctly"
        if len(information)==0:
            raise IndexError("not found information")  
        for dic in information:
            if dic['department']== criteria:
                name = dic['name']
                previous_salary = dic['salary']
                new_salary = [dic_new['salary'] for dic_new in new_information if dic_new['name']==name]   
                print(f'{name} salary was {previous_salary}$ and is now {new_salary[0]}$')
    except IndexError:
        print("Please enter the empoloyee information correctly")
# Give a raise of $10,000 to employees who meet the criteria of being in the Sales department
new_employees = give_raise(employees, 'Sales', 10_000)
# Print the new and old information of employees who meet thecriteria
print_employees(employees, new_employees, 'Sales')

# dictionary with the words and definitions
from random import choice
import sys

WORDS = {
"Absence": "The lack or unavailability of something orsomeone.",
"Approval": "Having a positive opinion of something or someone.",
"Answer": "The response or receipt to a phone call, question, or letter.",
"Attention": "Noticing or recognizing something of interest.",
"Amount": "A mass or a collection of something",
"Borrow": "To take something with the intention of returning it after a period of time.",
"Baffle": "An event or thing that is a mystery and confuses.",
"Ban": "An act prohibited by social pressure or law.",
"Banish": "Expel from the situation, often done officially.",
"Banter": "Conversation that is teasing and playful.",
"Characteristic": "referring to features that are typical to the person, place, or thing.",
"Cars": "Four-wheeled vehicles used for traveling.", "Care": "extra responsibility and attention.", 
"Chip": "a small and thin piece of a larger item.",
"Cease": "to eventually stop existing.",
"Dialogue": "A conversation between two or more people.",
"Decisive": "a person who can make decisions promptly.",
}

def messege():
    txt_messege = "1. Review random word\n2. Test yourself\n3. Exit"
    while True:
        try:  
            print(txt_messege)
            choice_user = int(input("Enter your choice: "))
            
            if choice_user > 3 or choice_user < 1:
                raise IndexError("invalid option")
            
            if choice_user == 1:
                Review_random_word()
            elif choice_user == 2:
                Test_yourself()
            elif choice_user == 3:
                print('Thank for use program learn english')
                break
        except ValueError :
            print("invalid option")
        except IndexError:
            print("invalid option")

def Review_random_word():
    word, definition = choice(list(WORDS.items()))
    print(f'Word: {word}\nDifinition: {definition}\n{"-"*20}')

def Test_yourself():
    word, definition = choice(list(WORDS.items()))
    
    sys.stdout.write(f"difinition: {definition}")
    sys.stdout.flush()
    time.sleep(5)
    sys.stdout.write('\r' + ' ' * len(f"difinition: {definition}") + '\r')
    sys.stdout.flush()
    
    number_attempt = 3
    while True:
        word_guessed = input('Enter the word: ').title()
        number_attempt -=1
        
        if word_guessed == word : 
            print("Bravoooooo you guesse word 👌👌👌")
            break
        else:
            pl_or_sn = ['attempt' if number_attempt==1 else 'attempts']
            print(f'incorrect answer, you have {number_attempt} {pl_or_sn[0]} remaining.')
        
        if number_attempt == 0:
            print(f"{'-'*20}\nthe correct answer is {word}")
            break

messege()
