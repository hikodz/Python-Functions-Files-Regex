import time
import sys

def show_and_remove_text(text, time_sleep):
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(time_sleep)
    sys.stdout.write('\r' + ' ' * len(text) + '\r')
    sys.stdout.flush()

# Usage
show_and_remove_text("my name is: hany shehab", 5)
