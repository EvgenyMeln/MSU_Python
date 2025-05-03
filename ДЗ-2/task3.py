str = input()
pos = str.find('/')
pos1 = str.find('/', pos+2)
str_new = str[pos+2:pos1]
print(str_new)
