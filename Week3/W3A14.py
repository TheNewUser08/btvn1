a = float(input())
b = float(input())

if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    x = -b / a
    if x == 0:
        x = 0.0
    print(f"{x:.2f}")
