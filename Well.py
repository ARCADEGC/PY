import math


try:
    pi = float(math.pi)
    h = float(input("\n\n\t  Depth of the well is: "))
    r = float(input("\n\n\t  Radius of the well is: "))
    a = float(input("\n\n\t  Surface of the water is: "))

except ValueError:
    print("\n\n\t Value must be a number! \n\n")
    exit()


o = (h - a) * (pi * pow(r, 2))
print("\n\n\t | There is ≈ %.2f" % o, "m³ | \n\n")
exit()