# Helper functions
import datetime as dt


# FUNCTION DEFINITIONS
def askTaskChoice():
    choice = input(
        """Choose your task:
Enter 1 to make new enteries
Enter 2 to update enteries
"""
    )
    return choice

    # ANIMAL parent class CODE


def askAnimalChoice():
    choice = input(
        """Which animal would you like to choose? 
Enter 'a' for chicken
Enter 'b' for cows
Enter 'c' for sheep"""
    )
    return choice


# Use Python's built-in datetime module
def age(birthdate):  # argument passed as datetime
    """This functioni is supposed to take in mm/yy date and return age in months"""
    pass


# OBJECT DEFINITIONS
class ANIMAL:
    animal = "XYZ"

    def __init__(self, animal):
        self.id = int(input(f"Chose unique ID for {animal}: "))
        # calculting age of animal from date of birth
        self.dob = tuple(map(int, input("dd/mm/yy of birth :").split()))
        self.age = age(self.dob)
        self.weight = float(input("Weight in kgs: "))
        # using datetime library we convert string input of date to datetime object for later use...
        self.strDate = input("Enter last vaccination data as dd/mm/yy: ")
        self.lastVaxDate = dt.datetime.strptime(
            self.strDate, "%d/%m/%y"
        )  # last vaccination date


class CHICKEN(ANIMAL):
    animalType = "chicken"

    def __init__(self):
        super().__init__(animal="chicken")
        self.last_7_days = [0, 0, 0, 0, 0, 0, 0]  # this list is used as a queue.
        print(f"{CHICKEN.animalType} object was created")

    # this is the function for weekly checkup and updates.
    # def weekly_checkup():

    def egg_production(self):  # this function should update the database
        todays_production = int(input(f"{self.id} has laid an egg today. Enter y/n : "))
        if todays_production == "y" or "Y":
            self.last_7_days.append(todays_production)
            self.last_7_days.pop(0)
        elif todays_production == "n" or "N":
            self.last_7_days.append(0)  # 0 is numbre of eggs
            self.last_7_days.pop(0)  # 0 is index of last_7_days
        else:
            todays_production == None
        return self.last_7_days

    def info(self):
        L = {
            "id": self.id,
            "age": self.age,
            "weight": self.weight,
            "last_vax_date": self.lastVaxDate,
            "last_7_days": self.last_7_days,
        }
        return L


class COW(ANIMAL):
    animalType = "cow"

    def __init__(self):
        super().__init__(animal="cow")
        self.last_7_days = [0, 0, 0, 0, 0, 0, 0]
        self.weekly_milk_production = sum(self.last_7_days)  # ? ? ?
        print(f"{COW.animalType} object was created")

    def milk_production(self):  # this function should update the database
        self.todays_production = float(
            input(f"Liters of milk {self.id} produced today: ")
        )
        print(" Input can only be a real number. Try again. ")
        self.last_7_days.pop(0)
        self.last_7_days.append(self.todays_production)
        return self.last_7_days

    def info(self):
        L = {
            "id": self.id,
            "age": self.age,
            "weight": self.weight,
            "last_vax_date": self.lastVaxDate,
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
        print(f"{SHEEP.animalType} object was created")

    def sheering_update(self):
        self.last_6_months = float(
            input(f"Wool (in kg) produced by {self.id} in last shearing: ")
        )
        self.weight = float(input(f"Weight (in kg) of {self.id} after shearing: "))

    def info(self):
        L = {
            "id": self.id,
            "age": self.age,
            "weight": self.weight,
            "last_vax_date": self.lastVaxDate,
            "last_7_days": self.last_6_months,
        }
        return L


"""
def Animal1(animalType):
animal = animalType
ID = int(input(f"Chose unique ID for {animal}: "))
age = int(input(f"Age of {animal} in Months: "))
weight = float(input("Weight in kgs: "))
# using datetime library we convert string input of date to datetime object for later use...
strDate = input("Enter last vaccination data as dd/mm/yy: ")
lastVaxDate = dt.datetime.strptime(strDate, '%d/%m/%y') #last vaccination date
def Chicken():
Animal1('chicken')
egg_production =
"""
