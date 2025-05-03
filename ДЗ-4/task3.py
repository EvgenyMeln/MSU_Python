s = input()
a = [float(x) for x in s.split()]
b1 = a[0]
q = a[1]
N = a[2]
s = (b1 * (q**N - 1)) / (q-1)
print(f"{s:.3f}")
