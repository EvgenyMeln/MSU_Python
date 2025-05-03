str_1 = input()
str_2 = input()
if str_1 == str_2:
    print("A")
elif str_1 in str_2:
    print("B")
elif str_2 in str_1:
    print("C")
else:
    print("D")
