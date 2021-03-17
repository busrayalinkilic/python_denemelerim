message= "Hello there. My name is Busra Yalinkilic".split()

# my_list = [1,2,3]
# my_list= ["bir", 2, True, 5.6]
# print(my_list)

list1= ["one","two", "three"]
list2= ["four", "five", "six"]

numbers= list1 + list2
print(numbers)  #hepsini tek bir liste içinde gösterir
print(len(numbers)) #eleman sayısı
print(message[0]) #sonunda ki split bunu liste haline getirir ve 0. eleman hello olur

userA = ["Sadık", 36]
userB = ["Busra", 21]
users= [userA, userB] #liste içinde liste elemanları
print(userA)
print(userB)
print(users)
print(users[1])
print(users[1][0]) #1. indexin içinde ki 0. eleman