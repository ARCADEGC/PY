try:
    num = int(input("What is num: "))
except ValueError:
    print("\n\t num must be a number! ")

step = 0
while True:
    if num < (step * 9):
        print(f"\n\n\t Value is {num - ((step * 9) - 9)}")
        exit()
    step += 1