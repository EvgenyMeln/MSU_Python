f = open("input.txt", encoding='utf8')
line = f.readlines()
f.close()

words = line[0].split()
for str in words:
    print(str[ : :-1], end = " ")
