ten = input().split()[3:]
so_thang_truoc = int(input().split()[-1])
so_thang_nay = int(input().split()[-1])
so_dien = so_thang_nay - so_thang_truoc
tien = 0

if so_dien >= 401:
    tien += (so_dien -401) * 3460 + 3350 * 100 + 2998 * 100 + 2380 * 100 + 2050 * 50 + 1984 * 50
elif so_dien >= 301:
    tien +=  3350 * (so_dien - 301) + 2998 * 100 + 2380 * 100 + 2050 * 50 + 1984 * 50
elif so_dien >= 201:
    tien +=  2998 * (so_dien - 201) + 2380 * 100 + 2050 * 50 + 1984 * 50
elif so_dien >= 101:
    tien +=  2380 * (so_dien -101) + 2050 * 50 + 1984 * 50
elif so_dien >= 51:
    tien +=  2050 * (so_dien - 51) + 1984 * 50
else:
    tien += so_dien * 1984


tien = 1.08 * tien

print("Ho va ten: " + " ".join(ten))
print("So tien phai tra la " + str(tien))
