message = "Hello there. My name is Busra Yalinkilic"
#message= message.upper()    #tüm karakterleri büyük harfe çevirir
# message= message.lower()     #küçük harfe çevirir
#message= message.title()   #her kelimenin baş harfi büyük olur
#message= message.capitalize()  #sadece ilk harf büyük oldu


#message= message.strip() #başlangıçta eğer bir boşluk karakteri varsa ki ben şuan ekledim, onu yok etmek için kullanılır
#message= message.split()  #cümleyi parçalara ayırdı. Çıktı:['Hello', 'there.', 'My', 'name', 'is', 'Busra', 'Yalinkilic']
#message= message.split('.') #noktadan itibaren ayıracak. Çıktı: [' Hello there', ' My name is Busra Yalinkilic']

#message= "*".join(message) #ayrı olarak gelen bilgileri tekrar birleştirmek istiyoruz. tırnak içine koyduğumuz şey arasına eklenir

# cümle içinde kelimenin varlığını kontrol etmek için:

# index=message.find("Busra")
# print(index)  #çıktı 25 oluyor çünkü aradığı kelimenin ilk harfinin index numarası 25 
# #eğer -1 çıksaydı bu kelimenin cümle içerisinde olmadığını gösterir

#isFound = message.startswith("H") #bu cümle h harfi ile mi başlıyor onu kontrol ediyoruz
# isFound = message.endswith("c") #bitiş harfi için
# print(isFound) #true ya da false döndürür

# message= message.replace("Busra", "Zeynep")   #büşrayı arayacak ve büşra yerine zeynep yazacak
# message= message.replace(" ", " & ")  # boşluk karakterleri yerine & koy
# #bunu türkçe karakterleri değiştirmek için kullanabiliriz mesela ç yerine c yaz gibi

message= message.center(100,"*")  #bizim için bir container oluşturur ve tam ortaya yerleştirir. 
#yanına " " içinde bir karakter eklersek cümleden önce ve sonra o karakter basar

""" DİĞER STRİNG METODLAR İÇİN:  google>string methods python"""
print(message)
#print(message[2]) #split komutu ile birlikte kullanıldığında 2. tırnak içinde ki ifadeyi alır yani my