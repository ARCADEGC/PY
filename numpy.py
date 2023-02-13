import numpy as np
from os import system
from time import sleep

# fuctions

def clear():
    system("cls")

def dtype_length(dt):
    match dt:
        case "i":
            return 4
        case "f":
            return 8
        case "U":
            return 25

# a title and inputs to generate a field

clear()
print("\n\n\t Welcome ti n-field generator usign NumPy!")
sleep(1)

try:
    x = int(input("\n\n Input the lenght of X dimension: "))
    y = int(input("Input the height of Y dimension: "))
    z = int(input("Input the depth of Z dimension: "))
    dt = input("Input data type (Int; Float; U character): ")
    fill = int(input("Do you want to fill the field with a numbers: "))
    if fill == 1:
        io = int(input("Do you want to fill it with ones (1), zeros (0) or random values (2): "))
    sort = int(input("Do you want to sort the field: "))
except ValueError:
    print("Invalid input!")

# field generation



if fill == 1:
    if io == 0:
        arr = np.zeros((x,y,z), dtype=np.dtype("{dt}{dtype_length(dt)}"))
    elif io == 1:
        arr = np.ones((x,y,z), dtype=np.dtype("{dt}{dtype_length(dt)}"))
    else:
        arr = np.random((x,y,z), dtype=np.dtype("{dt}{dtype_length(dt)}"))
else:
    arr = np.empty((x,y,z), dtype=np.dtype("{dt}{dtype_length(dt)}"))

if sort == 1:
    np.sort(arr)