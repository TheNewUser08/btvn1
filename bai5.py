kitu = input("Nhập vào 1 kí tự")

if len(kitu) == 1 and ord(kitu) > 91 and ord(kitu) <= 122:
    print(ord(kitu) + 31)
else:
    print("Đây là 1th đặc biệt")
