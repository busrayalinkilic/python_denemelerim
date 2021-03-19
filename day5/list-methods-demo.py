names = ["Ali", "Yagmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

# 3- "Deniz" ismini listeden siliniz
# names.remove("Deniz")
# print(names)

# 4- "Deniz" isminin indexi nedir?
index = names.index("Deniz")
names.pop(index)
print(index)

# 5- "Ali" listenin bir elemanı mıdır?
result = "Ali" in names
result = names.index("Ali")
print(result)

# 6- Liste elemanlarını ters çevirin
names.reverse()
years.reverse()
print(names)
print(years)

# 7- Liste elemanlarını alfabetik olarak sırala
names.sort()
print(names)

# 8- years listesini sayısal olarak sırala
years.sort()
print(years)

# 9- str= "Chervolet, Dacia" karakter dizisini listeye çeviriniz
str= "Chervolet, Dacia"
result2 = str.split(",")
print(result2)    

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
val = min(years)
val2 = max(years)
# print(val) 
# print(val2)
print(val, val2)

# 11- years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını silin
years.clear()
print(years)

# 13- kullanıcıdan alacağınız 3 tane marka bilgisini listede saklayınız
markalar= []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)