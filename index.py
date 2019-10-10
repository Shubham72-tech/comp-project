import time
import getch

def mainMenu():
    print("a for all users")
    print("b for new user")
    option=getch.getch()
    return option

#main
mainMenu()