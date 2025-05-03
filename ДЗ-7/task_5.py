import math

def function(x: float) -> float:
    return math.sin(math.tan(1 + x/1000))

f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

supposed_error = 1.0e-6
N = int(lines[0])
boundaries = []
answer = []

for i in range(1, len(lines)):
    boundaries.append(float(lines[i].split()[0]))
    boundaries.append(float(lines[i].split()[1]))

for i in range(0,len(boundaries),2):
    left_boundary = boundaries[i]
    right_boundary = boundaries[i + 1]
    while right_boundary - left_boundary > 2*supposed_error:
        middle = (right_boundary + left_boundary) / 2
        if function(left_boundary) * function(middle) <= 0:
            right_boundary = middle
        else:
            left_boundary = middle
    answer.append(float((right_boundary + left_boundary) / 2))

formatted_answer = [f"{x:.6f}" for x in answer]

for number in formatted_answer:
    print(number)
