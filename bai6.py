a, b, c = map(float, input("Nhập 3 số a b c").split())

if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh của 1 tam giác")
else:
    print("Đây không là 3 cạnh của 1 tam giác")
