col = 9
duck = 7
duck -= 1

string = "5 2 1 4 0 1 2 1 6"
strings = string.split()
field = [int(x) for x in strings]

if duck + 1 == col:
    field.append(max(field) + 1)
pointer = field[duck] + 1
dist = 0
n = 1
sum = 0
right = duck + dist
while right - n >= 0:
    right = duck + dist
    if pointer <= field[right]:
        while right - n >= 0:
            if pointer < field[right - n]: 
                pointer = field[right - n]

            sum += pointer - field[right - n]
            n += 1
    else:
        dist += 1
        
print(sum)