from collections import Counter

f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

animals = Counter()

for line in lines:
    animals[line.split()[1]] += 1

animals = animals.most_common()

for key, value in animals:
    print(key, value, sep = " - " )
