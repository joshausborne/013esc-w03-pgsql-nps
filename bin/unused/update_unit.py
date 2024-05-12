#!/usr/bin/env python3

from config import *

def clear():
    """
    Clear the screen in between activities
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Menu:
    """
    Define the construction of the menu.
    """
    def __init__(self):
        self.options = {}
        self.setPrompt("Please choose an option:")
        self.setErrorText("Error! Please enter a valid option.")

    def addOption(self, optionNumber, optionName, option, triggersExit):
        self.options[optionNumber] = [optionName, option, triggersExit]

    def setErrorText(self, errorText):
        self.errorText = errorText

    def setPrompt(self, prompt):
        self.prompt = prompt

    def size(self):
        return len(self.options)

    def displayError(self):
        print(f"\n{self.errorText}\n")

    def display(self):
        print(self.prompt)
        for i in range(1, self.size()+1):
            print(f"{i} - {self.options[i][0]}")
        print()

    def run(self):
        userInput = ""
        self.display()
        while True:
            userInput = input("Select a Task: ")
            try:
                userInput = int(userInput)
                if userInput <= 0 or userInput > self.size():
                    self.displayError()
                else:
                    if callable(self.options[userInput][1]):
                        self.options[userInput][1]()
                        if self.options[userInput][2]:
                            return
                        self.display()
                    else:
                        self.options[userInput][1].run()
                        self.display()
            except ValueError:
                self.displayError()

def exitOption():
    print("\nGood Bye!\n")

def returnOption():
    return

def display_unit(unit):
    unit_query = (('SELECT id, name, url, flyto_lat, flyto_long, flyto_heading, flyto_range, flyto_tilt '
                   f'FROM units WHERE id = \'{unit}\''))
    cursor.execute(unit_query)
    records = cursor.fetchall()
    id,name,url,flyto_lat,flyto_long,flyto_heading,flyto_range,flyto_tilt = records[0]
    print(f'Id: {id}\nName: {name}\nURL: {url}\n'
          f'Flyto Coordinates:\n '
          f'  Latitude: {flyto_lat}\n '
          f'  Longitude: {flyto_long}\n '
          f'  Heading: {flyto_heading}\n '
          f'  Range: {flyto_range}\n '
          f'  Tilt: {flyto_tilt}')


# Build the menu

def main():
    """
    The Main Menu is dynamically built. It has an index number, the name of the option, the
    function that it calls.
    """
    mainMenu = Menu()
    mainMenu.setPrompt("\nSelect a National Park:")

    menu1 = Menu()
    menu1.setPrompt("\nSelect a task:")
    menu1.addOption(1,"View Info",view_arch,False)
    menu1.addOption(2,"Edit Info",edit_arch,False)
    menu1.addOption(3,"Return",returnOption,True)

    menu2 = Menu()
    menu2.setPrompt("\nEdit Unit:")
    menu2.addOption(1,"Name",edit_name,False)
    menu2.addOption(2,"URL",edit_url,False)
    menu2.addOption(3,"Latitude",edit_latitude,False)
    menu2.addOption(4,"Longitude",edit_longitude,False)
    menu2.addOption(5,"Heading",edit_heading,False)
    menu2.addOption(6,"Range",edit_range,False)
    menu2.addOption(7,"Tilt",edit_tilt,False)
    menu2.addOption(8,"Return",returnOption,True)

    mainMenu.addOption(1,"Arches National Park",menu1,False)
    mainMenu.addOption(2,"Bryce Canyon National Park",menu1,False)
    mainMenu.addOption(3,"Canyonlands National Park",menu1,False)
    mainMenu.addOption(4,"Capitol Reef National Park",menu1,False)
    mainMenu.addOption(5,"Zion National Park",menu1,False)
    mainMenu.addOption(6,"Exit",exitOption,True)
    mainMenu.run()

def edit_name():
    print("you have selected edit_name")

def edit_url():
    print("you have selected edit_url")

def edit_latitude():
    print("you have selected edit_latitude")

def edit_longitude():
    print("you have selected edit_longitude")

def edit_heading():
    print("you have selected edit_heading")

def edit_range():
    print("you have selected edit_range")

def edit_tilt():
    print("you have selected edit_tilt")

def view_arch():
    """
    The view_arch function.
    """
    clear()
    display_unit('arch')
    
def edit_arch():
    """
    The edit_arch function.
    """
    clear()
    print("You have chosen the edit_arch function")
    display_unit('arch')

def view_brca():
    """
    The view_brca function.
    """
    clear()
    print("You have chosen the view_brca function")
    display_unit('brca')

def view_cany():
    """
    The view_cany function.
    """
    clear()
    print("You have chosen the view_cany function")
    display_unit('cany')

def view_care():
    """
    The view_care function.
    """
    clear()
    print("You have chosen the view_care function")
    display_unit('care')

def view_zion():
    """
    The view_zion function.
    """
    clear()
    print("You have chosen the view_zion function")
    display_unit('zion')


if __name__ == "__main__":
    main()

