# W2A10 [Friend Names]
names = input().split()
while len(names) < 3:
    names.extend(input().split())
print(f"Hi {names[2]}, {names[1]} and {names[0]}.")
