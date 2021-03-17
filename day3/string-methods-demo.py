website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python programlama Rehberiniz (40 saat)"
# 1- " Hello World " karakter dizininin baş ve sondaki boşlukları silin
message1 = " Hello World"
message1= message1.strip()
# message1 = message1.lstrip() #sadece soldaki boşluk karakteri
# message1 = message1.rstrip() #sadece sağdaki boşluk karakteri silinir 
# parantez içinde "" içerisinde silmek istediğimiz karakerleri yazıp silebiliriz
print(message1)

# # 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin
message2 = "www.sadikturan.com"
message2 = message2.split(".")
print(message2[1])

# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın
course = course.lower()
print(course)

# 4- "website" içinde kaç tane a karakteri vardır? (count("a"))
result= website.count("a") #arama alanı, birden fazla karakter erayabiliriz
print(result)

 # 5- "website" "www" ile başlayıp "com" ile bitiyor mu?
isFound= website.startswith("www")
isFound1= website.endswith("com")
print(isFound, isFound1)


# # 6- "website" içinde ".com" ifadesi var mı?
index=website.find(".com")
print(index)

# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
x= course.isalpha()   #ya da x=course.isdigit()
print(x)

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekle

message3= "Contents"
message3= message3.center(50,"*") 
#sadece soluna yerleştirmek istersek message3.ljust(50,"*") sağ istersek rjust
print(message3)

# 9- "course" tüm boşluk karakterlerini "-" ile değiştir.

# course=course.replace(" ", "-")
#print(course)

# 10- message1 de "world" yerine "There" yaz
message1 = message1.replace("World", "There")
print(message1)

# 11- "course" karakter dizisini boşluk karakterlerinden ayırın

course= course.split(" ")
print(course)