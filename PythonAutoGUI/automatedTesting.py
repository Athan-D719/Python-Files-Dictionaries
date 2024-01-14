import pyautogui as gui
from time import sleep
from random import choice as rc

class Automated_Test(object):
    status = str()
    wont = ['Nope', 'Nein', 'Niet', 'DadGammit', "M'boy"]

    def __init__(self, path):
        print("Welcome, master~")
        sleep(1)
        if './' not in path:
            self.status = "NOT in a million years"
            return "Absolute path needed"
        else:
            self.path = path
            print("You have (5) seconds to move to the terminal.")
            sleep(5)
            self.status = "Start the program"
        
    def get_script(self):
        try:
            with open(self.path) as inputs:
                sleep(0.5)         
                for i in inputs.readlines():
                    sleep(0.1)
                    # print(i[:-1])
                    gui.typewrite(i)
            self.status = "Finished"
        except Exception as e:
            print(rc(self.wont))
            print(e)
            self.status = "Error."

    def __str__(self):
        return "Status: {0}".format(self.status)

output = Automated_Test("./inputs.csv")
print(output)
output.get_script()
print(output)
