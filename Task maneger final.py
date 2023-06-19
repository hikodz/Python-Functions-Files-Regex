from datetime import datetime
import time
tasks = []
print("-------Hello In Task Maneger Program-------")
def intro_task_maneger():
    while True:
        try:
            
            input_choice = int(input('1. Add task to list\n2. Mark task as complete\n3. View tasks\n4. Quit\nEnter your choice: '))
            if input_choice > 4 or input_choice < 1:
                raise IndexError('🟥.invaild chioce')
            
            if input_choice ==1:
                add_task()
            elif input_choice ==2:
                mark_task_complete()
            elif input_choice ==3:
                view_taks()
            elif input_choice==4:
                show_result()
                break
        except ValueError:
            print('🟥.Please enter a number not string 🆎')
        except IndexError:
            print('🟥.Invalid choice, Please enter a number between 1 and 4 ⭕️')

# function for add task :
def add_task():
    while True:
        try:
            input_add_task = input("🟩.Please enter your task for back enter 'B' 🔖: ")
            if input_add_task.title()=='B':
                print('🟩.Retreat succeeded!!')
                return
            if input_add_task.isdigit()== True:
                raise TypeError('input user is all number')
            break
        except TypeError:
            print("🟥.Please enter a task that contains letters, not numbers")
    
    while True:
        input_add_date = input("🟩.Please enter task date (yyyy-mm-dd)⌚️ for back enter 'B': ")
        if input_add_date.title() =='B':
            print('🟩.Retreat succeeded!!')
            return
        try:
            date_object = datetime.strptime(input_add_date, "%Y-%m-%d")
            input_add_date = date_object.strftime("%Y-%m-%d")  # Format date as yyyy-m-d
            break
        except ValueError:
            print("🟥.Incorrect data format, please enter a date in (yyyy-mm-dd) 📅")
    
    while True:
        try:
            input_time = input("🟩.Please enter exact time to complete the task 24-hour time(h:m) ⏰ for back enter 'B': ")
            if input_time.title() == 'B':
                print('🟩.Retreat succeeded!!')
                return
            time.strptime(input_time, '%H:%M')
            break
        except ValueError:
            print("🟥.Incorrect time format, please enter a time in (h:m) ⏰")
    task = {'Task':input_add_task, 'Date':input_add_date, 'Time': input_time, 'Status': False }
    tasks.append(task)
    print('🟩.Task added to list 🔐')
        

# function for mark task complete
def mark_task_complete():
    try:
        
        reserved_tasks = [task for task in tasks if task['Status']==False]
        if len(reserved_tasks) > 0:
            
            for index, task in enumerate(reserved_tasks, 1):
                print(f"📍{index}. {task['Task'].title()}")
            input_for_mark = int(input('Please, enter the number of the task to mark as complete 🟢: '))
            if input_for_mark > len(reserved_tasks) or input_for_mark < 1:
                print('🟥.Invailed task number!!💤')
                return
            reserved_tasks[input_for_mark-1]['Status'] = True
            print('🟩.Task completed 🔓')
        else:
            print("🟥You don't have task for mark, Please add task 📝 and try again!!!")
    except ValueError:
        print('🟥Please enter a number 🔧')
    
    
# function view task:
def view_taks():
    if len(tasks) > 0:
        for index, task in enumerate(tasks, 1):
            emoji_status = '🔴' if task['Status']== False else '🟢'
            print(f"{emoji_status} {index}. {task['Task'].title()} ({task['Date']}) ({task['Time']})")
    else:
        print("🟥.You don't have task for view, Please add task 📝 and try again!!!")

# function for show messege if choice exit
def show_result():
    
    if len(tasks) == 0:
        print("You are lazy today, you did not add any task, you a loser boy 👎👎👎👎")
        print("Thank 😠😠 for use programe (TASK MENEGER) have a nice day loser boy!!😡😡😡")
    else:
        check_task_us = ['complete' for task in tasks if task['Status']== True]
        if len(tasks) == len(check_task_us):
            print("Good boy, you finish all task 👌")
            print("Thank for use programe (TASK MENEGER) have a nice day you are a hero 🫡")
        else:
            print("Not bad.Try to complete the remaining task another time today")
            reserved_tasks = [task for task in tasks if task['Status']==False]
            for index, task in enumerate(reserved_tasks, 1):
                print(f"📍{index}. {task['Task'].title()}")
            print("👆don't forget to complete the tasks 🤭🤭🤭 Thank for use programe (TASK MENEGER)")

# call function choices :         
intro_task_maneger()
