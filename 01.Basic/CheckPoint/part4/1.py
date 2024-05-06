PcPrice = { "HP" : 600 , "DELL" : 650 , "MACBOOK" : 1200 , "ASUS" : 400}
print("Total price :",PcPrice["ASUS"]*5)

a = input("Input a brand :")
b = int(input("Input amount to buy :"))
print("Total price :",PcPrice[a]*b)

pc = { "HP" : 20 , "DELL" : 50 , "MACBOOK" : 12 , "ASUS" : 30}

pc[a] = pc[a] - b
[print(f" {i}:{pc[i]}") for i in pc]