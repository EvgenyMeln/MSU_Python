f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

lines = sorted(
    [x.split('/t') for x in filter(lambda x: len(x), lines)],
    key = lambda x: (-ord(x[2]), int(x[1])),
    reverse = True
)

lines = '\n'.join(
