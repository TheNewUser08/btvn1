a = int(input())
b = int(input())
c = int(input())
d = int(input())

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d

print(largest)
