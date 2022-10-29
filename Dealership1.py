import sys

ListOfCars = ['Honda', 'Toyota', 'Mazda', 'Jeep', 'Lexus', 'BMW']

def mainMenu():
    while True:
        print()
        print('''### Welcome to Majed's Dealership ###
        Select a number for the action that you would like to do:
        1. Search Car
        2. Buy Car
        q --> quit
        ''')
        selection = input("Make your selection: ")
        if selection == "q":
            print("Thank you and have a good day!")
            break
        elif selection == "1":
            Search()
        elif selection == "2":
            Delete()
        else:
            print("You did not make a valid selection.")

def Delete():
    print("In order to buy the car it has to be in stock")
    SearchCar = input("What is the make of the car you want to buy? ")
    print("If it's in stock then you can buy it")
    if SearchCar in ListOfCars:
        ListOfCars.remove(SearchCar)
        print("The car ",SearchCar," is your now")
        return mainMenu()
    else:
        print("Sorry, ",SearchCar, " was already bought")
        return mainMenu()

def Search():
    print("In order to start the search for the car you want, we first need to check if it's in stock.")
    SearchCar = input("What is the make of the car you are looking today? ")
    print("Okay let me see if it's in stock")
    if SearchCar in ListOfCars:
        print("Yes, we have" , SearchCar , "in stock.")
        return mainMenu()
    else:
        print("Sorry ", SearchCar , " is not in stock")
        return mainMenu()

if __name__ == '__main__':
    mainMenu()
    