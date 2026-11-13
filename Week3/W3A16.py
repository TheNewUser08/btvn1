n = float(input())

floor_val = int(n // 1)
frac = n - floor_val

ceil_val = floor_val if frac == 0 else floor_val + 1

if n >= 0:
    nearest_val = floor_val + 1 if frac >= 0.5 else floor_val
else:
    nearest_val = floor_val + 1 if frac > 0.5 else floor_val

print(ceil_val, floor_val, nearest_val)
