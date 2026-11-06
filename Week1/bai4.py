kitu = input("Nhập vào 1 kí tự")

if len(kitu) == 1 and ord(kitu) >= 65 and ord(kitu) <= 122:
    print("Đây là 1 kí tự")
else:
    print("Đây không phải là một kí tự")
