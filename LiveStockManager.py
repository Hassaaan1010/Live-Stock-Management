"""READ ME
All data is stored in json 3 files
Objects for each type of animal are created.
start with making object types for cows, chickens, and sheep. 
the application is strictly limited to everyday record keeping and vax info...
(creating new objects is a small task so we can allow that)

for each object, say chicken001
store information about its age/DOB, weight, egg production in the last 7 days, next date for vaccination, and parasite/health check.
for each object, according to the updates, we can display what needs to be done (for example, if the parasite health check is negative thrice in a row, the output will recommend a check up....
make task that is used for daily production of egg for each chicken and update a queue[] of len:7
Exception handling for user input NOT DONE
"""

import datetime as dt
import json
from helperFunctions import *


def retrieve_data_from_files():
    """READ ME
    (This funciton is not defined in helperFuncitons.py because there was some issue with file accessing...)
    The entire data form <animal>_data.json file is stored into <animal>Data variable
    This variable is returned to <animal>_data variable during function call
    All the alterations are made in the application are made to <animal>_data variable
    At the end of the program the new <animal>_data is written back into the same file.
    """
    chickenFileObject = open("chickenData.json", "r+")
    chickenData = json.load(chickenFileObject)

    cowFileObject = open("cowData.json", "r+")
    cowData = json.load(cowFileObject)

    sheepFileObject = open("sheepData.json", "r+")
    sheepData = json.load(sheepFileObject)

    return (
        chickenFileObject,
        chickenData,
        cowFileObject,
        cowData,
        sheepFileObject,
        sheepData,
    )


def return_data_to_files():
    # rewrite all files by storing updated form of <animal>_data dictionary into json file
    update_files(chicken_file_object, chicken_data)
    update_files(cow_file_object, cow_data)
    update_files(sheep_file_object, sheep_data)

    print("\n\nAll data has been updated :) \n")


# PROGRAM STARTS HERE

# retrieving data from files
(
    chicken_file_object,
    chicken_data,
    cow_file_object,
    cow_data,
    sheep_file_object,
    sheep_data,
) = retrieve_data_from_files()


print("Welcome to LiveStockManager.py \n")


application_choice = True
while application_choice == True:
    TaskChoice = askTaskChoice()
    if TaskChoice == "new":
        new_entry_continue = True
        while new_entry_continue == True:
            # USER CHOSE TO MAKE NEW ENTERIES
            AnimalChoice = askAnimalChoice()
            if AnimalChoice == "chicken":
                newEntry(chicken_data, "chicken")
            elif AnimalChoice == "cow":
                newEntry(cow_data, "cow")
            elif AnimalChoice == "sheep":
                newEntry(sheep_data, "sheep")
            new_entry_continue = askExit("making new entries")

    elif TaskChoice == "update":
        # USE WANTS TO UPDATE ENTERIES
        update_enteries_continue = True
        while update_enteries_continue == True:
            AnimalChoice = askAnimalChoice()
            if AnimalChoice == "chicken":
                # user wants to update CHICKENS
                #   HOW DO I ACCESS AND CALL FUNCTIONS FOR OBJECTS IF I USED dummy FOR INPUT
                for a_chicken in chicken_data:
                    this_chicken = chicken_data[a_chicken]
                    print(this_chicken["id"])
                    egg_production(this_chicken)
            elif AnimalChoice == "cow":
                for a_cow in cow_data:
                    this_cow = cow_data[a_cow]
                    print(this_cow["id"])
                    milk_production(this_cow)
            elif AnimalChoice == "sheep":
                for a_sheep in sheep_data:
                    this_sheep = sheep_data[a_sheep]
                    print(this_sheep["id"])
                    sheering_update(this_sheep)
            update_enteries_continue = askExit("updating entries")

    elif TaskChoice == "delete":
        # USER WANTS TO DELETE ENTERIES
        delete_entry_continue = True
        while delete_entry_continue == True:
            AnimalChoice = askAnimalChoice()
            if AnimalChoice == "chicken":
                deleteEntery(chicken_data, "chicken")
            elif AnimalChoice == "cow":
                deleteEntery(cow_data, "cow")
            else:
                deleteEntery(sheep_data, "sheep")
            delete_entry_continue = askExit("deleting entries")

    application_choice = askExit("managing livestock")

return_data_to_files()
