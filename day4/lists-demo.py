# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına saip bir liste oluşturun
# list1= ["Bmw", "Mercedes", "Opel", "Mazda"]
# print(list1)

# # 2- Liste kaç elemanlıdır?
# print(len(list1))

# # 3- Listenin ilk ve son elemanı nedir?
# print(list1[0])
# print(list1[3])

# # 4- Mazda değerini Toyota ile değiştirin
# list1.append("Toyota")
# list1.remove("Mazda")
# print(list1)

#bir diğer seçenek list1[-1]= "Toyota"

# # 5- Mercedes listenin bir elemanı mıdır?
# index = "Mercedes" in list1
# print(index)

# # 6- Listenin -2 indexindeki değer nedir?
# print(list1[-2])

# # 7- listenin ilk 3 elemanını alın
# print(list1[0:3])

# # 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
# list1[-2:] = ["Toyota", "Renault"]
# print(list1)

# # 9-Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
# list1.append("Audi")
# list1.append("Nissan")
# print(list1)

# # 10- listenin son elemanını silin
# del list1[-1]
# print(list1)

# # 11- Listenin elemanlarını tersten yazın
# result= list1[::-1]
# print(result)

# 12- Aşağıdaki verileri bir liste içinde saklayınız
      
      # studentA: Yigit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan 1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)

studentA= ["Yigit", "Bilgi", 2010, [70,60,70]]
studentB= ["Sena", "Turan", 1999, [80,80,70]]
studentC= ["Ahmet", "Turan", 1998, [80,70,90]]


# 13- Liste elemanlarını ekrana yazdırın
ogrenciler= studentA + studentB + studentC
print(ogrenciler)


# 14- Yiğitin yaşını ve ortalamasını bul
result = studentA[0]
result = studentB[1]
result = studentC[3][1]
result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)

