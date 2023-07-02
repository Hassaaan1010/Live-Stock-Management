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
from datetime import datetime, timedelta
import json
from helperFunctions import *
from termcolor import colored


def retrieve_data_from_files():
    """READ ME
    (This funciton is not defined in helperFuncitons.py because there was some issue with file accessing...)
    The entire data form <animal>_data.json file is stored into <animal>Data variable using json.load()
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

    miscFileObject = open("miscData.json", "r+")
    miscData = json.load(miscFileObject)

    return (
        chickenFileObject,
        chickenData,
        cowFileObject,
        cowData,
        sheepFileObject,
        sheepData,
        miscFileObject,
        miscData,
    )


def return_data_to_files():
    # rewrite all files by storing updated form of <animal>_data dictionary into json file
    update_files(chicken_file_object, chicken_data)
    update_files(cow_file_object, cow_data)
    update_files(sheep_file_object, sheep_data)
    update_files(misc_file_object, misc_data)

    print("\n\nAll data has been updated :) \n")


# DRIVER CODE

# retrieving data from files
(
    chicken_file_object,
    chicken_data,
    cow_file_object,
    cow_data,
    sheep_file_object,
    sheep_data,
    misc_file_object,
    misc_data,
) = retrieve_data_from_files()

# Update health checkup dates weekly
if getTodaysDate() >= misc_data["next_health_check_date"]:
    misc_data["last_health_check_date"] = misc_data["next_health_check_date"]
    misc_data["next_health_check_date"] = get_next_health_check_date(
        misc_data["last_health_check_date"]
    )


print("Welcome to LiveStockManager.py \n")
last_health_date = misc_data["last_health_check_date"]
next_health_date = misc_data["next_health_check_date"]

print(f"Last Health Checkup Date: {last_health_date}")
print(f"Next Health Checkup Date: {next_health_date}")
print_todays_vaccinations(chicken_data, cow_data, sheep_data)
get_vaccinations_done()

# health_check()yes

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
                deleteEntry(chicken_data, "chicken")
            elif AnimalChoice == "cow":
                deleteEntry(cow_data, "cow")
            else:
                deleteEntry(sheep_data, "sheep")
            delete_entry_continue = askExit("deleting entries")

    elif TaskChoice == "details":
        get_details_continue = True
        while get_details_continue == True:
            AnimalChoice = askAnimalChoice()
            if AnimalChoice == "chicken":
                showEntry(chicken_data, "chicken")
            elif AnimalChoice == "cow":
                showEntry(cow_data, "cow")
            else:
                showEntry(sheep_data, "sheep")
            get_details_continue = askExit("seeing entries")
    elif TaskChoice == "add":
        misc_data["last_health_check_date"] = input(f"Give me the date mfer: ")
        misc_data["flag"] = 1
        misc_data["next_health_check_date"] = get_next_health_check_date(
            misc_data["last_health_check_date"]
        )

    application_choice = askExit("managing livestock")

return_data_to_files()
