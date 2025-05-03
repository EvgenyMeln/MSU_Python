f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

Matrix = []

for line in lines:
    Matrix.append(line.split())

trans_Matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]

for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        trans_Matrix[j][i] = Matrix[i][j]

f_out = open("output.txt", "w", encoding='utf8')
for row in trans_Matrix:
    print(*row, file = f_out)
f_out.close()
