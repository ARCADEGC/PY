# funkce za vyčištění terminálu a import knihovny os
from os import system
def clear():
    system("cls")

# import knihovny NumPy pod názvem "np"
import numpy as np

# titulek
clear()
print("\n\n\t Numpy Array Generator/Modifier")

# volba generátoru
run = str(input("\n\t   [generate/modify] What do you want to do: "))

# požadavky na vytvoření pole
while run == "generate":
    try:
        array_type = str(input("\n\n\t [zeros/ones/empty/arange/linspace/exit] Array type: "))

        if array_type == "exit":
            exit()

        if array_type == "zeros" or array_type == "ones" or array_type == "empty":
            amount = int(input("\n\t How many values do you want: "))

        if array_type == "arange" or array_type == "linspace":
            start = float(input("\n\t Starting number: "))
            finish = float(input("\n\t Last number: "))
        if array_type == "arange":
            step = float(input("\n\t Step: "))
        elif array_type == "linspace":
            fit = int(input("\n\t Amount of numbers to fit: "))

        if array_type == "zeros" or array_type == "ones" or array_type == "empty":
            data_type = str(input("\n\t [int/float] What data type should the array be made out of: "))

    except ValueError:
        print("\n\t There has been a ValueError. Try again ...")
        
    #tvorba pole
    if array_type =="zeros" or array_type == "ones" or array_type == "empty":
        if array_type == "zeros":
            arr = np.zeros(amount, dtype=data_type)
        elif array_type == "ones":
            arr = np.ones(amount, dtype=data_type)
        elif array_type == "empty":
            arr = np.empty(amount, dtype=data_type)
        print(f"\n\t    np.{array_type}({amount}, dtype={data_type}) == {arr}")

    elif array_type == "arange":
        print(f"\n\t    np.{array_type}({start}, {finish}, {step}) == ", np.arange(start, finish, step))

    else:
        print(f"\n\t    np.{array_type}({start}, {finish}, {fit}) ==", np.linspace(start, finish, fit))

    # reshape
    reshape = str(input("\n\t [yes/no] Do you want to reshape your array: "))
    if reshape == "yes":
        try:
            height = int(input("\n\t Z axis: "))
            width = int(input("\n\t Y axis: "))
            depth = int(input("\n\t X axis: "))
        except ValueError:
            print("\n\t There has been a ValueError. Try again ...")
        
        print(f"\n\t    arr = np.reshape({height}, {width}, {depth}) == ", np.reshape(arr, (height, width, depth)))
    
# mofikace
while run == "modify":
    # požadavky
    try:
        modify_type = str(input("\n\n\t [unique/concatenate/sort/sum/reshape/size/shape/exit] What do you want to do: "))
        array = []
        n = int(input("\n\t Enter number of elements: "))
  
        for i in range(0, n):
            element = float(input())
            array.append(element)
        if modify_type == "concatenate":
            array2 = []
            n = int(input("\n\t Enter number of elements: "))
    
            for i in range(0, n):
                element = float(input())
                array2.append(element)
    except ValueError:
        print("\n\t There has been a ValueError. Try again ...")

    # samotná modifikace
    match modify_type:
        case "unique":
            # nefunkční
            print("\n\t arr = np.unique(arr) == ", np.unique((array)))
            # oficiální dokumentace
            # a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
            # unique_values = np.unique(a)
            # print(unique_values)
            # [11 12 13 14 15 16 17 18 19 20]         

        case "concatenate":
            print("\n\t arr = np.concatenate(arr, arr2) == ", np.concatenate((array, array2)))

        case "sort":
                print("\n\t arr = np.flip == ", np.sort(array))

        case "sum":
            print(f"\n\t    arr = np.sum == ", np.sum(array, dtype=np.float64))

        case "reshape":
            try:
                height = int(input("\n\t Z axis: "))
                width = int(input("\n\t Y axis: "))
                depth = int(input("\n\t X axis: "))
            except ValueError:
                print("\n\t There has been a ValueError. Try again ...")
            
            print(f"\n\t    arr = np.reshape({height}, {width}, {depth}) == ", np.reshape(arr, (height, width, depth)))

        case "size":
            print("\n\t arr = np.size == ", np.size(array))

        case "exit":
            exit()