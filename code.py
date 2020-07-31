import os
import sys
import time

with open("~/remindme/alarm.txt", "r+") as f:
    alarm = f.read()

method = sys.argv[1]
minutes = int(sys.argv[2]) # If it's a float, this will convert it

# validating minutes
if minutes == 0:
    print("I cannot remind you in 0 minutes")
    exit()


if method == "in":
    counter = minutes
    for _ in minutes:
        time.sleep(60)
        counter -= 1
        print(f"only {counter} minutes left")
        print()

    os.system(alarm)

elif method == "every":
    while True:
        counter = minutes
        for _ in minutes:
            time.sleep(60)
            counter -= 1
            print(f"only {counter} minutes left")
            print()

        os.system(alarm)

else:
    print("invalid command: read the README")
