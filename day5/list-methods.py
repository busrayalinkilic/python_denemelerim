numbers= [1, 10, 5, 16, 4, 9, 10]
letters= ["a","g","s", "b", "y", "a", "s"]

val = min(numbers)
val= max(numbers)
val= max(letters)
val= min(letters)

val= numbers[3:6]
val= numbers[:6]
val= numbers[4:]

numbers[4]= 40

numbers.append(49) #en sona ekler
numbers.insert(3, 78) #3. index artık 78 oldu diğerleri de kaydı
numbers.insert(-1,52) #en sondan 1 önceye ekler

numbers.pop() #en sonda ki sayı silindi
numbers.pop(0) # 0. indekteki eleman silindi
numbers.remove(52) #silmek istediğimiz sayıyı yazdık

numbers.sort() #küçükten büyüğe sıralanır
letters.sort() #alfabetik olarak sıralar
numbers.reverse() #tam tersine çevirir
letters.reverse()


# print(letters)
# print(numbers)  #bu listeler güncelleneilebilir

print(len(numbers))
print(len(letters))

print(numbers.count(10)) #kaç tane 10 var??
print(letters.count("a")) #kaç a var

numbers.clear() #tüm elemanları silmek için clear metodu kullanılır
print(numbers)
# print(val)