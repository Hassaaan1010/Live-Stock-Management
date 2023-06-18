# Helper functions
import datetime as dt
import json


# OBJECT DEFINITIONS
class ANIMAL:
    animal = "XYZ"

    def __init__(self, animal):
        self.id = input(f"Chose unique ID number for {animal}: ")
        # calculting age of animal from date of birth
        # self.dob = tuple(map(int, input("dd/mm/yy of birth :").split()))
        # self.age = age(self.dob)
        self.weight = float(input("Weight in kgs: "))

    # using datetime library we convert string input of date to datetime object for later use...
    # self.strDate = input("Enter last vaccination data as dd/mm/yy: ")
    # self.lastVaxDate = dt.datetime.strptime(
    # self.strDate, "%d/%m/%y"
    # ) last vaccination date


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
            # "age": self.age,
            "weight": self.weight,
            # "last_vax_date": self.lastVaxDate,
            "last_7_days": self.last_7_days,
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
            # "age": self.age,
            "weight": self.weight,
            # "last_vax_date": self.lastVaxDate,
            "last_7_days": self.last_7_days,
            "weekly_milk_production": self.weekly_milk_production,
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
            # "age": self.age,
            "weight": self.weight,
            # "last_vax_date": self.lastVaxDate,
            "last_6_months": self.last_6_months,
        }
        return L


# FUNCTION DEFINITIONS
def askTaskChoice():
    choice = (
        input(
            """Choose your task:
Enter 'new' to make new enteries 
Enter 'update' to update enteries
Enter 'delete' to delete enteries
"""
        )
        .lower()
        .strip()
    )
    if choice in ["new", "update", "delete"]:
        print("*" * 20)
        return choice
    else:
        print("Invalid input!")
        return askTaskChoice()


def askAnimalChoice():
    choice = (
        input(
            """Which animal would you like to choose? 
chicken
cow
sheep
 :- """
        )
        .lower()
        .strip()
    )
    if choice in ["chicken", "cow", "sheep"]:
        print("_" * 20)
        return choice
    else:
        print("Invalid input! Choose on of 'chicken','cow','sheep'")
        return askAnimalChoice()

    # Use Python's built-in datetime module
    # def age(birthdate):  # argument passed as datetime
    # """This functioni is supposed to take in mm/yy date and return age in months"""


def askExit(task):
    choice = (
        input(
            f"""Do you want to continue {task} ?
chose 'exit' or 'continue' """
        )
        .lower()
        .strip()
    )
    if choice in ["exit", "continue"]:
        if choice == "exit":
            return False
        else:
            return True
    else:
        print('Invalid input! Chose "exit" or "continue"')
        return askExit(task)


def egg_production(a_chicken_dictionary):
    # this function should update the database
    todays_production = int(
        input(f"{a_chicken_dictionary['id']}: Number of eggs laid : ")
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
    todays_production = float(
        input(f"Liters of milk cow {a_cow_dictionary['id']} produced today: ")
    )
    # print(" Input can only be a real number. Try again. ")
    a_cow_dictionary["last_7_days"].pop(0)
    a_cow_dictionary["last_7_days"].append(todays_production)
    a_cow_dictionary["weekly_milk_production"] = sum(a_cow_dictionary["last_7_days"])


def sheering_update(a_sheep_dictionary):
    a_sheep_dictionary["last_6_months"] = float(
        input(f"Wool (in kg) produced by sheep {a_sheep_dictionary['id']} : ")
    )
    a_sheep_dictionary["weight"] = float(
        input(f"Weight (in kg) of sheep {a_sheep_dictionary['id']} after shearing: ")
    )


def newEntry(animal_data_dictionary, AnimalChoice):
    N = int(input(f"How many new {AnimalChoice} enteries do you want? : "))
    for i in range(N):
        # dummy = animal_object_dictionary[AnimalChoice]

        if AnimalChoice == "chicken":
            dummy = CHICKEN()
        elif AnimalChoice == "cow":
            dummy = COW()
        else:
            dummy = SHEEP()

        animal_data_dictionary[dummy.id] = dummy.info()


def deleteEntery(animal_data_dictionary, AnimalChoice):
    selected_ID = input(
        f"""Enter ID number of {AnimalChoice} that is to be deleted: 
(Enter 'exit' if you want to quit) : """
    ).strip()
    if selected_ID in animal_data_dictionary:
        del animal_data_dictionary[selected_ID]
        print(f"{selected_ID} records deleted.\n")
    elif selected_ID.lower().strip() == "exit":
        pass
    else:
        print("ID not found!")
        print(f"here is a list of all the {AnimalChoice} enteries :\n")
        for id in list(animal_data_dictionary.keys()):
            print(id)
        deleteEntery(animal_data_dictionary, AnimalChoice)


def update_files(file_object, animal_data):
    file_object.seek(0)
    json.dump(animal_data, file_object)
    file_object.truncate()
    file_object.close()
