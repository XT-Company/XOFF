import sys
import time as t
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

"""
OS name = XOFF
name emulator = None
Version os = 0.1.1 Alpha
"""

def menu():
    clear()
    t.sleep(0.05)
    print("||======================================||")
    t.sleep(0.1)
    print("||  \\      /  ======    |=====   |===== ||")
    t.sleep(0.1)
    print("||   \\    /   |    |    |        |      ||")
    t.sleep(0.1)
    print("||    \\  /    |    |    |        |      ||")
    t.sleep(0.1)
    print("||      =     |    |    |====    |===== ||")
    t.sleep(0.1)
    print("||     / \\    |    |    |        |      ||")
    t.sleep(0.1)
    print("||    /   \\   |    |    |        |      ||")
    print("||   /     \\  ======    |        |      ||")
    print("||======================================||")

    print("\nWelcome\n-You are in the main menu for OS\n- In version 0.2 We add interface!")
    while True:
        command = input("> ")
        if command == 'exit':
          sys.exit(0)
        elif command == 'res':
            clear()
            t.sleep(0.05)
            print("||======================================||")
            t.sleep(0.1)
            print("||  \\      /  ======    |=====   |===== ||")
            t.sleep(0.1)
            print("||   \\    /   |    |    |        |      ||")
            t.sleep(0.1)
            print("||    \\  /    |    |    |        |      ||")
            t.sleep(0.1)
            print("||      =     |    |    |====    |===== ||")
            t.sleep(0.1)
            print("||     / \\    |    |    |        |      ||")
            t.sleep(0.1)
            print("||    /   \\   |    |    |        |      ||")
            print("||   /     \\  ======    |        |      ||")
            print("||======================================||")
            print("\nWelcome\n-You are in the main menu for OS\n- In version 0.2 We add interface!")
        elif command == 'info':
            print("Information:\nOS: XOFF\nVersion OS: 0.1.1 Alpha\nProduct: XT Comapny\nCreator: Matvey Burnashov")
        elif command == 'help':
            print("List of commands:\n - exit      -- exit from emulator\n - res         -- reset emulator (go back)")
            print(" - help         -- list of command\n - info        -- information about emulator OS\n - cls       -- clear console")
        elif command == 'cls':
            clear()
        else:
            print("!! Unknown command !!")

def start():
    clear()
    print("Started emulator!")
    t.sleep(2)
    print("\nOS name = XOFF")
    print("OS version = 0.1.1 Alpha")
    t.sleep(3)
    menu()
