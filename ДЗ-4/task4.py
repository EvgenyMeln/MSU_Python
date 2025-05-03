f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

minimum = 100.0
maximum = -100.0
N = int(lines[0])
for line in lines[1:]:
    for x in line.split():
        minimum = min(minimum, float(x))
    maximum = max(maximum, minimum)
    minimum = 100.0
 
print(f"{maximum:.3f}")
