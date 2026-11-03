kitu = input("Nhập 1 kí tự trong bảng chữ cái")

if len(kitu) == 1 and ord(kitu) >= 65 and ord(kitu) <= 122:
    if kitu.isupper():
        print(kitu.lower())
    elif kitu.islower():
        print(kitu.upper())
else:
    print("Đây không phải là một kí tự")

print(ord("A"))
print(ord("z"))
