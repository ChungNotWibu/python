Phone = {
    "Iphone12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000
}

a = input("Input name of a phone:")
try: 
    print(f"Price of {a}:", Phone[a])
except KeyError:
    print("Wrong phone brand name!")