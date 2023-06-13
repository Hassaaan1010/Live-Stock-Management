"""READ ME
All data is stored in json 3 files
Objects for each type of animal are created.
start with making object types for cows, chickens, and sheep. 
the application is strictly limited to everyday record keeping and vax info...
(creating new objects is a small task so we can allow that)
for each object, say chicken001
we can store information about its age/DOB, weight, egg production in the last 14 days, next date for vaccination, and parasite/health check.
for each object, according to the updates, we can use if-else conditions to keep we can display what needs to be done (for example, if the parasite health check is negative 3 times in a row, the output will recommend a check up by vets....
Maybe make a task that is used for daily production of egg for each chicken and update a queue[] of len:7
Exception handling for user input NOT DONE
"""

import datetime as dt
import json
from helperFunctions import *

CowList = ChickenList = SheepList = []  # COMMENT

# def retrieve_data_from_files():
chicken_file = open("chickenData.json", "r+")
chicken_data = json.load(chicken_file)
"""
the entire data form chicken_data.json file is stored here

all the alterations are made in the application are made to this variable

at the end of the program the new {chicken_data} is written back into the same file.
"""
cow_file = open("cowData.json", "r+")
cow_data = json.load(cow_file)
"""
the entire data form cow_data.json file is stored here

all the alterations are made in the application are made to this variable

at the end of the program the new {cow_data} is written back into the same file
"""
sheep_file = open("sheepData.json", "r+")
sheep_data = json.load(sheep_file)
"""
the entire data form sheep_data.json file is stored here

all the alterations are made in the application are made to this variable

at the end of the program the new {sheep_data} is written back into the same file
"""


# ch = chicken() #COMMENT
# c = cow()  #COMMENT
# s = sheep() #COMMENT
#########################################################

# PROGRAM STARTS HERE
# retrieve_data_from_files()
print("Welcome to LiveStockManager.py")

TaskChoice = askTaskChoice()
if TaskChoice == 1:
    # USER CHOSE TO MAKE NEW ENTERIES
    AnimalChoice = askAnimalChoice()
    if AnimalChoice == "a":
        N = int(input("How many chickens do you want to register?:"))
        for i in range(1, N + 1):
            dummy = CHICKEN()
            chicken_data["C" + str(i)] = dummy.info()

    elif AnimalChoice == "b":
        N = int(input("How many cows do you want to register?:"))
        for i in range(1, N + 1):
            dummy = COW()
            cow_data["C" + str(i)] = dummy.info()

    elif AnimalChoice == "c":
        N = int(input("How many sheep do you want to register?:"))
        for i in range(1, N + 1):
            dummy = SHEEP()
            sheep_data["C" + str(i)] = dummy.info()
        pass

    else:
        print("enter valid choice!")
        animalChoice = askAnimalChoice()

elif TaskChoice == 2:
    # USE WANTS TO UPDATE ENTERIES
    AnimalChoice = askAnimalChoice()

    AnimalChoice = askAnimalChoice()
    if AnimalChoice == "a":
        # user wants to update CHICKENS
        for i in chicken_data:
            #                                   HOW DO I ACCESS AND CALL FUNCTIONS FOR OBJECTS IF I USED dummy FOR INPUT
            pass
    elif AnimalChoice == "b":
        pass
    elif AnimalChoice == "c":
        pass

    else:
        print("enter valid choice!")
        animalChoice = askAnimalChoice()
else:
    print("enter valid choice!")
    TaskChoice = askTaskChoice()
