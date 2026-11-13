a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")
