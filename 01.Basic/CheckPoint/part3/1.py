PcPrice = { "HP" : 600 , "DELL" : 650 , "MACBOOK" : 1200 , "ASUS" : 400}

print("Price of ASUS:",PcPrice["ASUS"])

a = input("Input a brand:")
print(f"Price of {a}:",PcPrice[a])
