import random

base = float(random.randint(1, 9))
num = base

while (base != 10):

    print("\n\t Base is:", base)
    operant = input("\n\t What is the operator: ")

    if (operant == "*"):
        base *= num
    if (operant == "/"):
        base /= num
    if (operant == "+"):
        base += num
    if (operant == "-"):
        base -= num