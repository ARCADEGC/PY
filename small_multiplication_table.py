run = 1
print("\n\t For exit() set the multiples or number value to 0.")


while run == 1:

    repeat = 1
    while repeat == 1:
        try:
            requested_steps = int(input("\n\n\t Requested multiples: "))
            if (requested_steps == 0):
                print("\n\n\t End. \n")
                exit()

            requested_numbers = int(input("\n\n\t Requsted numbers: "))
            if (requested_numbers == 0):
                print("\n\n\t End. \n")
                exit()
            repeat = 0
        except ValueError:
            print("\n\n\t !!\t Values must be numbers! \t!! \n\n")
    print("\n\n")


    num = int(2)
    while num <= requested_numbers:
        step = 1

        while (step <= requested_steps):
            if int(len(str(requested_steps * requested_numbers))) > 3: 
                print("{: >4}".format(num * step), end=" ")
            else:
                print(" ", "{: >3}".format(num * step), end=" ")
                
            step += 1

        print("\n")
        num += 1