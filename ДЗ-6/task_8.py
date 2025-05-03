from collections import defaultdict

f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

animals = defaultdict(list)

for line in lines:
    animals[line.split()[1] + ":"].append(line.split()[0])

animals = sorted(animals.items(), key = lambda pair: len(pair[0]))

for i in range(len(animals)):
    animals[i][1].sort()

for key, value in animals:
    print(key, ', '.join(value))
