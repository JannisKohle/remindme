import os
import sys
import time

alarmPath = os.path.expanduser("~/remindme/alarm.txt")
with open(alarmPath, "r+") as f:
    alarm = f.read()

method = sys.argv[1]
minutes = int(sys.argv[2]) # If it's a float, this will convert it

# validating minutes
if minutes == 0:
    print("I cannot remind you in 0 minutes")
    exit()


if method == "in":
    counter = minutes
    for _ in range(minutes):
        time.sleep(60)
        counter -= 1
        if counter != 0:
            print(f"only {counter} minutes left")
            print()

    os.system(alarm)

elif method == "every":
    while True:
        counter = minutes
        for _ in range(minutes):
            time.sleep(60)
            counter -= 1
            if counter != 0:
                print(f"only {counter} minutes left")
                print()

        os.system(alarm)

else:
    print("invalid command: read the README")
