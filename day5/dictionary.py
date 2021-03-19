# # (liste tipi)   key - value şeklinde
# #mesela 34=> istanbul

# #dictionary olmadan nasıl yaparız:
# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41, 34]

# print(plakalar[sehirler.index("kocaeli")])
# print(plakalar[sehirler.index("istanbul")])   

# #dictionary kullanarak:
# # print(plakalar["kocaeli"]) => 41 olması lazım

# #plakalar = { "key" : "value", ...}
# plakalar = { "kocaeli" : 41, "istanbul" : 34 }
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6 #ankara key olarak eklenir
# plakalar["kocaeli"] = "new value" #yeni değer atanır
# print(plakalar)

users = {
    "sadikturan" : {
        "age" : 36,
        "roles" : ["user"],
        "email" : "ss@.com",
        "address" : "kocaeli",
        "phone" : "11111"


    },
    "cinarturan" : {
        "age" : 2,
        "roles" : ["admin", "user"],
        "email" : "cc@.com",
        "address" : "kocaeli",
        "phone" : "11111"
    }
}

print(users["cinarturan"])
print(users["cinarturan"]["age"])
print(users["cinarturan"]["email"])
print(users["cinarturan"]["roles"][0])