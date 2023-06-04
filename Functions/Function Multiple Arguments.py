# during definition inputs are called parameters
# during function call inputs are called arguments
# Lesson 3 - Function Multiple Arguments
#Section 12: Python Functions, Files & Regex
# exercise part 1:
pizzas = {
    "Margherita": 120,
    "Pepperoni": 200,
    "Hawaiian": 150,
    "Meat Lovers": 250,
    "Mushroom": 140,
}
def pizza():
    for name, price in pizzas.items():
        print(f'{name:12}: {price} EGP')
pizza()
# exercise part 2:
def print_employee_info(name="codezilla", age=25, salary=10_000, section=None):
    print(f"Name: {name.title()}") 
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    print(f"Section: {section}")

# 1.
print_employee_info("Mohamed ahmed", 25, 10_000) 
# 2.
print_employee_info(name="hassan Ali", age=33, salary=15_000)
# 3.
print_employee_info(age=30, name="Ali Hassan", salary=20_000)
# 4.
print_employee_info("Ahmed Mohamed", salary=15_000, age=35) 
# 5.
print_employee_info("Hazem Khaled", salary=15_000)
# 6.
print_employee_info(age=25, name="Hamed Ali", salary=14_000)
# 7.
print_employee_info("Mohamed khedr", salary=13_000, age=25, section="IT")
# exercise part 3:
def print_students_info(name, age, city="Cairo", school="Codezilla"):
    print(f"Name: {name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")
    print(f"School: {school.title()}")

print_students_info("Ahmed Mohamed", 25)
print_students_info("Mohamed Ahmed", 33, "cairo", "Al-Azhar")
print_students_info("Ali Hassan", 30, "Alexandria")
print_students_info("Hazem Khaled", 35, "New York", "Khaled ibn al-Walid")
print_students_info("Hamed Ali", 25, "Tanta", "Al Durra")
# exercise part 4:
name = "hamada codezilla"
grades = {
    "math": 99,
    "english": 98,
    "science": 99,
    "arabic": 100,
    "history": 99
}
def print_student(name_student, grades_student, school='codezilla'):
    print(f'Student: {name_student.title()}')
    print(f'School: {school}')
    txt='Grades'
    print(f'{txt:.^20}')
    for sub, grade in grades_student.items():
        print(f'{sub.title()}: {grade}')
print_student(name, grades)
