pc = { "HP" : 20 , "DELL" : 50 , "MACBOOK" : 12 , "ASUS" : 30}

print("Available MACBOOKs :",pc["MACBOOK"])

a = input("Input a brand :")
try:
    print(f"Available {a}s :", pc[a])
except KeyError:
    print("Wrong pc brand name!")