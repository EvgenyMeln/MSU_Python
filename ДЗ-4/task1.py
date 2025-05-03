base = 2
s = ""
x = int(input())
if x == 0:
    print(0)
while x != 0:  # пока икс "не закончился"
    digit = x % base
    s += str(digit)
    x = x // base
print(s[::-1])
