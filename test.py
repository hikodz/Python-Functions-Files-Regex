import time

def timer(time_user):
    for i in range(time_user, 0, -1):
        print(i, end="\r")
        time.sleep(1)
user_time = int(input('Please enter the number of seconds to start setting the timer: '))
timer(user_time)

# reverse timer 
import time

def timer(time_user):
    for i in range(1, (time_user+1)):
        print(i, end="\r")
        time.sleep(1)
user_time = int(input('Please enter the number of seconds to start setting the timer: '))
timer(user_time)