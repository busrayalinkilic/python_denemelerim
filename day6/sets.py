fruits = {"banana", "grape", "cherry"}
print(fruits)  # elemanların yerleri karışık geliyor hatta her çalıştırmada sıra değişiyor.

#   print(fruits[0])  #hata verdi çünkü indekslenemez

#elemanlarına ulaşmak için döngü kullanırız

for x in fruits:
    print(x)   # bu şekilde sırayla her eleman x e yazılır ama liste SIRALANAMAZ

#eleman ekleme:
fruits.add("apple")
fruits.update(["mango", "orange"]) #birden fazla eleman eklemek için, var olan apple ı yazsak tekrarlanmazdı. 
#Liste içerisinde her elemandan yalnızca bir tane vardır.

#eleman silme:
fruits.remove("mango") #veya;
fruits.discard("apple") #veya;
fruits.pop()  #normalde son elemanı siler ama burada belli bir sıra olmadığı için herhangi biri silinir

#tüm elemanları silmek için;
fruits.clear()

print(fruits)

myList = [1,2,5,4,4,2,1]
print(set(myList))  #sete çevirince tekrarlanan elemanlar çıktı da görünmez
print(myList)  #liste olduğu gibi görünür




