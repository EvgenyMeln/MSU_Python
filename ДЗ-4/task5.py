f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

minimum = 10 ** 10 ** 2
limit  = int(lines[0].split()[0])
N  = int(lines[0].split()[1])
cost = 0
flag = False

for line in lines[1:]:
    for pair in line.split():
        n = pair.find('/')
        price = int(pair[:n])
        quantity = int(pair[n+1:])
        if price <= limit:
            minimum = min(minimum, price * quantity)
            flag = True
    if flag == False:
            minimum = 0
    cost += minimum
    flag = False
    minimum = 10 ** 10 ** 2

print(cost)
