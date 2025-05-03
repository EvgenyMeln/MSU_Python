s = input()
for i in range(len(s)):
    if s[i] == "X":
        c = "A"
    elif s[i] == "Y":
        c = "B"
    elif s[i] == "Z":
        c = "C"
    elif s[i] == "x":
        c = "a"
    elif s[i] == "y":
        c = "b"
    elif s[i] == "z":
        c = "c"
    elif "A" <= s[i] < "X":
        c = chr((ord(s[i]) + 3))
    elif "a" <= s[i] < "x":
        c = chr((ord(s[i]) + 3))
    else:
        c = s[i]
    print(c, end = "")
