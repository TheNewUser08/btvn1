# W2A11 [Hours and Minutes to Seconds]
vals = input().split()
while len(vals) < 2:
    vals.extend(input().split())
h, m = map(int, vals[:2])
print(h * 3600 + m * 60)
