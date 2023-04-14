from time import time

from os import system
def clear():
    system("cls")

def key_maker():
    key = "J", "a", "r", "o", "m", "i", "r", "1", "2", "3"
    lskey = []
    for char in key:
        lskey.append(ord(char))
    return lskey

key = key_maker()

start_time = time()
clear()
n = 0
ls = [33]
while True:
    i = 1
    while i <= len(ls):
        try:
            ls[0] = 33
            while ls[0] < 126:
                if ls == key:
                    string = ""
                    for character in ls:
                        string += chr(character)
                    print(f"\n\n\t The PASS is | {string} | \n")
                    end_time = time()
                    print(f"\n\n\t It took {end_time - start_time} seconds!")
                    exit()
                ls[0] += 1

            n = 0
            while True:
                if ls[n] == 126:
                    ls[n] = 33
                    n += 1
                else:
                    index = n
                    break
            ls[index] += 1
        except IndexError:
            break

    ls.append(33)
    for reset in range(len(ls)):
        ls[reset] = 33