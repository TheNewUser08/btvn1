# W2A3 [ModAndDiv]
vals = input().split()
while len(vals) < 2:
    vals.extend(input().split())
a, b = map(int, vals[:2])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(f"{a / b:.2f}")
