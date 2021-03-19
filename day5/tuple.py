list = [1, 2, 3]

tuple = (1, "iki", 3)

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ["ali", "veli"]
tuple = ("damla", "ayşe")   # içlerine yeni eleman ekliyoruz. (var olanları silip)
names = ("demet", "emel", "ayşe") + tuple
print(names) # çıktı:('demet', 'emel', 'ayşe', 'damla', 'ayşe')

list[0] = "ahmet" # bu işlemi tuple için yapamıyoruz. Eleman ataması yapılmaz. TEK FARK
#tuple üzerinde count (bir karakterin kaç tane olduğu) ve index(nerede olduğunu) kullanılabilir


print(list)
print(tuple)