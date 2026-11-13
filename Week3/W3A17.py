a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    print("Yes" if b == 0 and c == 0 and d == 0 else "No")
elif b % a == 0:
    q = b // a
    print("Yes" if b * q == c and c * q == d else "No")
else:
    print("No")
