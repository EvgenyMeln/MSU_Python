f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

boys = []

for line in lines:
    boy = []
    boy.append(line.split()[0])
    boy.append(float(line.split()[1])) if "." in line.split()[1] else boy.append(int(line.split()[1]))
    boys.append(boy)

boys.sort(reverse = True, key = lambda x: x[1])

boys_1 = boys[0:23:2]
boys_2 = boys[1:23:2]

f_out = open("output.txt", "w", encoding='utf8')
for boy in boys_1:
    print(*boy, file = f_out)
for boy in boys_2:
    print(*boy, file = f_out)
f_out.close()

