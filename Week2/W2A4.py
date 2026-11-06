# W2A4 [AverageOfSix]
a1, b1, c1, a2, b2, a3 = map(float, input().split())
tb = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print(f"{tb:.1f}")
