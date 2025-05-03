f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

animals_male = set()
animals_female = set()

for line in lines:    
    if line.split()[2] == "male":
        animals_male.add(line.split()[1])
    else:
        animals_female.add(line.split()[1])

animals = animals_male & animals_female

if not animals:
    print(0)
else:
    print(*sorted(animals, key = lambda x: len(x)), sep = '\n')
