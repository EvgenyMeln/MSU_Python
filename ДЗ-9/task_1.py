import itertools as it

x = (False, True)

for x_1, x_2, x_3 in it.product(x, repeat = 3):
    if (not x_1 and x_2 and not x_3) or (not x_1 and x_2 and x_3) or (x_1 and not x_2 and not x_3):
        print(x_1, x_2, x_3)
