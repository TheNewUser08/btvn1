n = int(input())
reversed_n = 0
if 99 < n < 1000:
    for i in range(3):
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    print(reversed_n)
else:
    print("So can co 3 chu so")
