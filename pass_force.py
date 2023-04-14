from random import randint
def code_gen():
    return randint(0, 99_999_999)

from os import system
def clear():
    system("cls")


clear()
key = 0
code = code_gen()

while True:
    key += 1
    if key == code:
        print(f"\n\n\t Code is: {key} \n\n")
        exit()