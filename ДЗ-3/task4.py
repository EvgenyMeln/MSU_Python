f_in = open("input.txt", encoding='utf8')
lines = f_in.readlines()
f_in.close()

N = int(lines[0])
names = lines[1:N+1]
dates = lines[N+1:]
print(names)
f_out = open("output.txt", "w", encoding='utf8')
for x, y in zip(names, dates):
    x = x.replace("\n", "")
    y = y.replace("\n", "")
    print(x, y, sep = '\t', file = f_out)
f_out.close()
