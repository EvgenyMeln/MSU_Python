f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

lines.sort(key = lambda x: len(x.split()))

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = " ".join(sorted(lines[i].split(), key = len))

f_out = open("output.txt", "w", encoding='utf8')
for line in lines:
    print(*line, sep = '', file = f_out)
f_out.close()
