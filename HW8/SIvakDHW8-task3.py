import random

the_number = random.randint(1, 50)
choice = int(input("Enter estimated number from 1 to 50: "))
tries = 10
while choice != the_number:
    if choice > the_number:
        print("Try a smaller number")
    else:
        print("Try a larger number")
    if tries == 0:
        break
    choice = int(input("Estimated number: "))
    tries -= 1
if choice != the_number:
    print("NO MORE ATTEMPTS!")
else:
    print("Yeap, you are GUESS!")

import json
import datetime

def get(number, trials):
    dict = {"Number": the_number, "Trials": trials, "Time": str(datetime.datetime.now())}
if int(choice) == the_number:
    with open("info.json", "w") as file:
        json.dump(dict, file, indent=4)