f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

A_calls = []
B_calls = []

for line in lines:
    if line.split('\t')[2] == "A":
        A_calls.append(line.strip().split('\t'))
    else:
        B_calls.append(line.strip().split('\t'))

A_calls_answer = sorted(A_calls, key = lambda x: int(x[1]), reverse = True)

for i in range(len(A_calls)):
    A_calls_answer[i] = '\t'.join(A_calls_answer[i])

B_calls_answer = sorted(B_calls, key = lambda x: int(x[1]), reverse = True)

for i in range(len(B_calls)):
    B_calls_answer[i] = '\t'.join(B_calls_answer[i])

f_out = open("output.txt", "w", encoding='utf8')
for line in A_calls_answer:
    print(*line, sep = '', file = f_out)
for line in B_calls_answer:
    print(*line, sep = '', file = f_out)
f_out.close()
