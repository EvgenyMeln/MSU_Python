from collections import Counter

f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

digits_frequencies = Counter()

for digit in lines[0]:
    digits_frequencies[digit] += 1

digits_frequencies = sorted(digits_frequencies.items(), key = lambda pair: (pair[1], int(pair[0])))

print(digits_frequencies[0][0])
    
