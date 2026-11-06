# W2A13 [Unit Digit of Product]
vals = input().split()
while len(vals) < 2:
    vals.extend(input().split())
a, b = map(int, vals[:2])
print((a * b) % 10)
