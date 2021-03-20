x, y, z =2, 5, 10

numbers = 1, 5, 7, 10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# sayi1 = int(input("1. sayi: "))
# sayi2 = int(input("2. sayi: "))

# # toplam =  x + y + z 
# # carpim = sayi1 * sayi2
# # fark = carpim - toplam
# fark = (sayi1 * sayi2) - (x+y+z)
# print(fark)

# 2- y'nin x'e kalansız bölümünü hesaplayınız
result = y // x
print(result)

# 3- (x,y,z) toplamının mod 3 ü nedir?
result = (x+y+z) % 3
print(result)

# 4- y'nin x. kuvvetini hesaplayınız
result = y ** x
print(result)

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır
x, *y, z = numbers
print(x, y, z)
result = z ** 3
print(result)

# 6- aynı işleme göre y'nin değerleri toplamı nedir

result = y[0] + y[1] + y[2]
print(result)
