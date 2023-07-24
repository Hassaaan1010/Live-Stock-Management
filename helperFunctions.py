# Helper functions
import datetime as dt
import json
from datetime import datetime, timedelta
from termcolor import colored


miscFileObject = open("miscData.json", "r+")
misc_data = json.load(miscFileObject)


# OBJECT DEFINITIONS
class ANIMAL:
    animal = "XYZ"

    def __init__(self, animal):
        self.id = input(f"Chose unique ID number for {animal}: ")

        self.weight = float(input("Weight in kgs: "))

        self.dobSTR = input("Enter date of birth in format dd/mm/yy: ")
        self.dob = datetime.strptime(self.dobSTR, "%d/%m/%y")

        self.lastVaxDate = datetime.strptime(
            input("Enter dd/mm/yy of last vaccination :"), "%d/%m/%y"
        )
        self.lastVaxDateSTR = self.lastVaxDate.strftime("%d/%m/%y")

        self.nextVaxDate = self.lastVaxDate + timedelta(days=3 * 30)
        self.nextVaxDateSTR = self.nextVaxDate.strftime("%d/%m/%y")
        self.health_status = input(f"Enter Health Status of Animal-{self.id}: ")


class CHICKEN(ANIMAL):
    animalType = "chicken"

    def __init__(self):
        super().__init__(animal="chicken")
        self.last_7_days = [0, 0, 0, 0, 0, 0, 0]  # this list is used as a queue.
        print(f"{CHICKEN.animalType} object was created\n")

    # this is the function for weekly checkup and updates.
    # def weekly_checkup():
    def info(self):
        L = {
            "id": self.id,
            "DOB": self.dobSTR,
            "weight": self.weight,
            "last_vaccination_date": self.lastVaxDateSTR,
            "next_vaccination_date": self.nextVaxDateSTR,
            "last_7_days": self.last_7_days,
            "health_status": self.health_status,
        }
        return L


class COW(ANIMAL):
    animalType = "cow"

    def __init__(self):
        super().__init__(animal="cow")
        self.last_7_days = [0, 0, 0, 0, 0, 0, 0]
        self.weekly_milk_production = sum(self.last_7_days)  # ? ? ?
        print(f"{COW.animalType} object was created\n")

    def info(self):
        L = {
            "id": self.id,
            "DOB": self.dobSTR,
            "weight": self.weight,
            "last_vaccination_date": self.lastVaxDateSTR,
            "next_vaccination_date": self.nextVaxDateSTR,
            "last_7_days": self.last_7_days,
            "weekly_milk_production": self.weekly_milk_production,
            "health_status": self.health_status,
        }
        return L


class SHEEP(ANIMAL):
    animalType = "sheep"
    # Wool is sheared every 6 months

    def __init__(self):
        super().__init__(animal="sheep")
        self.last_6_months = int(
            input(f"Wool (in kg) produced by {self.id} in last shearing: ")
        )
        print(f"{SHEEP.animalType} object was created\n")

    def info(self):
        L = {
            "id": self.id,
            "DOB": self.dobSTR,
            "weight": self.weight,
            "last_vaccination_date": self.lastVaxDateSTR,
            "next_vaccination_date": self.nextVaxDateSTR,
            "last_6_months": self.last_6_months,
            "health_status": self.health_status,
        }
        return L


# FUNCTION DEFINITIONS


def getTodaysDate():
    # returns todays date as dd/mm/yy string
    date = datetime.today().date()
    formated_date = date.strftime("%d/%m/%y")
    return formated_date


def getNewDate(today):
    "gets a date 90 days from today"
    last_vacc = today  # Example last vaccination date

    # Convert the last_vacc string to a datetime object
    last_vacc_date = datetime.strptime(last_vacc, "%d/%m/%y")

    # Calculate the next vaccination date as exactly 3 months after last_vacc
    next_vacc_date = last_vacc_date + timedelta(days=3 * 30)

    # Convert the next_vacc_date to the desired format (DD/MM/YY)
    next_vacc = next_vacc_date.strftime("%d/%m/%y")

    return next_vacc


def askTaskChoice():
    if misc_data["flag"] == 0:
        alert_date_init = colored(
            "Enter 'add' to initialize last health checkup date",
            "red",
            attrs=["blink"],
        )
        print(
            colored(
                f"""Choose your task:
{alert_date_init}
Enter 'new' to make new entries 
Enter 'update' to update entries
Enter 'delete' to delete entries
Enter 'details' to get details of an entry
""",
                "blue",
                attrs=["bold"],
            )
        )
    else:
        print(
            colored(
                """Choose your task:
Enter 'new' to make new entries 
Enter 'update' to update entries
Enter 'delete' to delete entries
Enter 'details' to get details of an entry
""",
                "blue",
                attrs=["bold"],
            )
        )
    choice = input().lower().strip()

    if misc_data["flag"] == 0 and choice in [
        "new",
        "update",
        "delete",
        "details",
        "add",
    ]:
        print("*" * 20)
        return choice
    elif misc_data["flag"] == 1 and choice in ["new", "update", "delete", "details"]:
        print("*" * 20)
        return choice
    else:
        print(colored("Invalid input!", "red", attrs=["underline"]))
        return askTaskChoice()


def askAnimalChoice():
    print(
        colored(
            """Which animal would you like to choose? 
chicken
cow
sheep
 :- """,
            "green",
            attrs=["bold"],
        )
    )
    choice = input().lower().strip()
    if choice in ["chicken", "cow", "sheep"]:
        print("_" * 20)
        return choice
    else:
        print(
            colored(
                "Invalid input! Choose one of 'chicken','cow','sheep'",
                "red",
                attrs=["underline"],
            )
        )
        return askAnimalChoice()

    # Use Python's built-in datetime module
    # def age(birthdate):  # argument passed as datetime
    # """This functioni is supposed to take in mm/yy date and return age in months"""


def askExit(task):
    print(
        colored(
            f"""Do you want to continue {task} ?
chose 'exit' or 'continue' """,
            "red",
            attrs=["dark"],
        )
    )
    choice = input().lower().strip()
    if choice in ["exit", "continue"]:
        if choice == "exit":
            return False
        else:
            return True
    else:
        print(
            colored(
                'Invalid input! Chose "exit" or "continue"', "red", attrs=["underline"]
            )
        )
        return askExit(task)


def egg_production(a_chicken_dictionary):
    # this function should update the database
    todays_production = int(
        input(
            colored(f"{a_chicken_dictionary['id']}: Number of eggs laid : ", "yellow")
        )
    )
    last_7_days = a_chicken_dictionary["last_7_days"]
    if todays_production > 0:
        last_7_days.append(todays_production)
        last_7_days.pop(0)
    elif todays_production == 0:
        last_7_days.append(0)  # 0 is numbre of eggs
        last_7_days.pop(0)  # 0 is index of last_7_days
    else:
        todays_production == None


def milk_production(a_cow_dictionary):  # this function should update the database
    print(
        colored(
            f"Liters of milk cow {a_cow_dictionary['id']} produced today: ", "yellow"
        )
    )
    todays_production = float(input())
    # print(" Input can only be a real number. Try again. ")
    a_cow_dictionary["last_7_days"].pop(0)
    a_cow_dictionary["last_7_days"].append(todays_production)
    a_cow_dictionary["weekly_milk_production"] = sum(a_cow_dictionary["last_7_days"])


def sheering_update(a_sheep_dictionary):
    print(
        colored(
            f"Wool (in kg) produced by sheep {a_sheep_dictionary['id']} : ", "yellow"
        )
    )

    a_sheep_dictionary["last_6_months"] = float(input())
    print(
        colored(
            f"Weight (in kg) of sheep {a_sheep_dictionary['id']} after shearing: ",
            "yellow",
            end="",
        )
    )
    a_sheep_dictionary["weight"] = float(input())


def newEntry(animal_data_dictionary, AnimalChoice):
    print(
        colored(
            f"How many new {AnimalChoice} enteries do you want? : ",
            "magenta",
            attrs=["underline"],
        )
    )
    N = int(input())
    for i in range(N):
        # dummy = animal_object_dictionary[AnimalChoice]

        if AnimalChoice == "chicken":
            dummy = CHICKEN()
        elif AnimalChoice == "cow":
            dummy = COW()
        else:
            dummy = SHEEP()

        animal_data_dictionary[dummy.id] = dummy.info()


def deleteEntry(animal_data_dictionary, AnimalChoice):
    print(
        colored(
            f"""Enter ID number of {AnimalChoice} that is to be deleted: 
(Enter 'exit' if you want to quit) : """,
            "light_red",
        )
    )
    selected_ID = input().strip()
    if selected_ID in animal_data_dictionary:
        del animal_data_dictionary[selected_ID]
        print(
            colored(
                f" records of {selected_ID} were deleted.\n",
                "red",
            )
        )
    elif selected_ID.lower().strip() == "exit":
        pass
    else:
        print(colored("ID not found!", "red", attrs=["underline"]))
        print(f"here is a list of all the {AnimalChoice} enteries :\n")
        for id in list(animal_data_dictionary.keys()):
            print(id)
        deleteEntry(animal_data_dictionary, AnimalChoice)


def update_files(file_object, animal_data):
    file_object.seek(0)
    json.dump(animal_data, file_object)
    file_object.truncate()
    file_object.close()


def showEntry(animal_data_dictionary, AnimalChoice):
    print(
        colored(
            f"""Enter ID number of {AnimalChoice}: 
(Enter 'exit' if you want to quit) : """,
            "light_green",
        )
    )
    selected_ID_details = input().strip()
    if selected_ID_details.lower().strip() == "exit":
        pass
    elif selected_ID_details in animal_data_dictionary:
        print(colored(f"Details of {selected_ID_details}: ", "light_green"))
        for detail in animal_data_dictionary[selected_ID_details]:
            print(f"\t{detail}: {animal_data_dictionary[selected_ID_details][detail]}")
    else:
        print(colored("ID not found!", "red", attrs=["underline"]))
        print(f"here is a list of all the {AnimalChoice} enteries :\n")
        for id in list(animal_data_dictionary.keys()):
            print(id)
        showEntry(animal_data_dictionary, AnimalChoice)


def print_todays_vaccinations(animal1_data, animal2_data, animal3_data):
    # prints due vaccination for each animal
    today = getTodaysDate()
    todays_list = {"chickens": [], "cows": [], "sheep": []}
    for animal1 in animal1_data:
        if animal1_data[animal1]["next_vaccination_date"] <= today:
            todays_list["chickens"].append(animal1_data[animal1]["id"])

            animal1_data[animal1]["last_vaccination_date"] = today
            animal1_data[animal1]["next_vaccination_date"] = getNewDate(today)

    for animal2 in animal2_data:
        if animal2_data[animal2]["next_vaccination_date"] <= today:
            todays_list["cows"].append(animal2_data[animal2]["id"])

            animal2_data[animal2]["last_vaccination_date"] = today
            animal2_data[animal2]["next_vaccination_date"] = getNewDate(today)

    for animal3 in animal3_data:
        if animal3_data[animal3]["next_vaccination_date"] <= today:
            todays_list["sheep"].append(animal3_data[animal3]["id"])

            animal3_data[animal3]["last_vaccination_date"] = today
            animal3_data[animal3]["next_vaccination_date"] = getNewDate(today)

    print(
        colored(
            f"List of vaccinations due for today ({today}): ",
            "yellow",
            attrs=[
                "underline",
            ],
        )
    )
    for animal in todays_list:
        print(colored(f"{animal} : {todays_list[animal]}", "yellow"))


def get_vaccinations_done():
    print(
        colored(
            """Have you completed all vaccinations due for today? 
Enter 'yes' or 'no'
""",
            "yellow",
            attrs=["underline"],
        )
    )
    status = input().lower().strip()
    if status in ["yes", "no"]:
        if status == "yes":
            return
        else:
            print(
                colored(
                    "Cannot proceed with application without completing vaccinations",
                    "red",
                    attrs=["underline"],
                )
            )
            get_vaccinations_done()
    else:
        print(colored("Invalid input!", "red", attrs=["underline"]))
        get_vaccinations_done()


def get_next_health_check_date(last_date):
    # Convert the last_vacc string to a datetime object
    last_health_check_date = datetime.strptime(last_date, "%d/%m/%y")

    # Calculate the next vaccination date as exactly 3 months after last_vacc
    next_health_check_date = last_health_check_date + timedelta(days=7)

    # Convert the next_vacc_date to the desired format (MM/YY)
    next_health_check_vacc = next_health_check_date.strftime("%d/%m/%y")
    return next_health_check_vacc
