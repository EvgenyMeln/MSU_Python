count = 0
suma = 0
s = ''
x = int(input())
while x != 0:
    x_bin = str(bin(x))
    if x_bin.count('0') == 4:
        count += 1
        suma += x
    x = int(input())
    
print(count, suma)
