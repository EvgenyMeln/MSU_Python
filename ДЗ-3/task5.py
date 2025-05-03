import itertools as it

f = open("input.txt", encoding='utf8')
line = f.readline()
f.close()

words = line.split()
for t in it.combinations(words, 3):
    print("1:", t[0], "2:", t[1], "3:", t[2])
