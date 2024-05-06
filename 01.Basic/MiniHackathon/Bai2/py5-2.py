Phone = {
    "Iphone12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000
}

a = int(input("Input your budget:"))
print("Phones that fit your budget:")

PhoneList = Phone.items()
[print(f'- {i[0]} : {i[1]}') for i in PhoneList if i[1] < a ]