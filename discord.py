from datetime import datetime
import time
tasks = []
def intro_task_maneger():
    while True:

        try:
            input_choice = int(input('1. Add task to list\n2. Mark task as complete\n3. View tasks\n4. Quit\nEnter your choice: '))
            if input_choice > 4 or input_choice < 1:
                raise IndexError('invaild chioce')
            
            if input_choice ==1:
                add_task()
            elif input_choice ==2:
                mark_task_complete()
            elif input_choice ==3:
                view_taks()
            elif input_choice==4:
                print("Thank for use programe (TASK MENEGER) have a nice day!!🫡")
                break
        
        except ValueError:
            print('Please enter a number not string 🆎')
        except IndexError:
            print('Invalid choice, Please enter a number between 1 and 4 ⭕️')

def add_task():
    
    input_add_task = input("Please enter your task 🔖: ")
   
    while True:
        input_add_date = input("Please enter task date (yyyy-mm-dd)⌚️: ")
        try:
            date_object = datetime.strptime(input_add_date, "%Y-%m-%d")
            input_add_date = date_object.strftime("%Y-%-m-%-d")  # Format date as yyyy-m-d
            break
        except ValueError:
            print("Incorrect data format, please enter a date in (yyyy-mm-dd) 📅")
    
    while True:
        try:
            input_time = input("Please enter exact time to complete the task 24-hour time(h:m) ⏰: ")
            time.strptime(input_time, '%H:%M')
            break
        except ValueError:
            print("Incorrect time format, please enter a time in (h:m) ⏰")
    task = {'Task':input_add_task, 'Date':input_add_date, 'Time': input_time, 'Status': False }
    tasks.append(task)
    print('Task added to list 🔐')
        


def mark_task_complete():
    try:
        reserved_tasks = [task for task in tasks if task['Status']==False]
        if len(reserved_tasks) > 0:
            
            for index, task in enumerate(reserved_tasks, 1):
                print(f"📍{index}. {task['Task'].title()}")
            input_for_mark = int(input('Please, enter the number of the task to mark as complete 🟢: '))
            if input_for_mark > len(reserved_tasks) or input_for_mark < 1:
                print('Invailed task number!!💤')
                return
            reserved_tasks[input_for_mark-1]['Status'] = True
            print('Task completed 🔓')
        else:
            print("You don't have task for mark, Please add task 📝 and try again!!!")
    except ValueError:
        print('Please enter a number 🔧')
    
    
    
def view_taks():
    if len(tasks) >0:
        for index, task in enumerate(tasks, 1):
            emoji_status = '🔴' if task['Status']== False else '🟢'
            print(f"{emoji_status} {index}. {task['Task'].title()} ({task['Date']}) ({task['Time']}) ")
    else:
        print("You don't have task for view, Please add task 📝 and try again!!!")



intro_task_maneger()

