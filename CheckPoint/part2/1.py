pc = { "HP" : 20 , "DELL" : 50 , "MACBOOK" : 12 , "ASUS" : 30}

newpc = {"TOSHIBA" : 10}
pc.update(newpc)
print("Available products:")
[print(f" {i}:{pc[i]}") for i in pc]

newpcname = input("Input a brand :")
newpcamount = input("Input amount :")
newpc2 = {newpcname : newpcamount}
pc.update(newpc2)
print("Available products:")
[print(f" {i}:{pc[i]}") for i in pc]

