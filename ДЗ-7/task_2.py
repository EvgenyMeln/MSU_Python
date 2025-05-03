import math

def f(day: int) -> float:
    return 20 * math.exp(math.sin(day/100) * day/10)

answer = f(18)
print(answer, int(answer))
