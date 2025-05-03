f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

animals = set()

for line in lines:
    animals.add(line.split()[1])

print(*sorted(animals, key = lambda x: len(x)), sep = '\n')
