# PYTHON

input = list(map(int, input()))
if len(input) == 1 and input[0] == 9:  # input is 9
    print(9)
else:
    has_nine = 9 in input  # check if input has at least one 9
    has_zero = 0 in input  # check if input has at least one 0
    if has_zero:
        input = [x for x in input if x != 0]  # remove all zeros from the input if there are zeros in the input
    if has_nine:
        input = [x for x in input if x != 9]  # remove all nines from the input if there are nines in the input
    while sum(input) > 9:
        input = list(map(int, str(sum(input))))
        has_nine = 9 in input  # check if current sum has at least one 9
        has_zero = 0 in input  # check if current sum has at least one 0
        if has_nine:
            input = [x for x in input if x != 9]  # remove all nines from the intermediate sums if there are nines in the current sum
        if has_zero:
            input = [x for x in input if x != 0]  # remove all zeros from the intermediate sums if there are zeros in the current sum
    print(sum(input))



# input = list(map(int, input()))
# while sum(input) >= 10:
#     intermediate_sum = 0
#     for x in input:
#         intermediate_sum += x
#     input = list(map(int, str(intermediate_sum)))
# print(sum(input))