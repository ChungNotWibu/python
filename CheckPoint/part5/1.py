pc = { "HP" : 20 , "DELL" : 50 , "MACBOOK" : 12 , "ASUS" : 30}
a = pc.get('HP')
b = pc.get('DELL')
c = pc.get('MACBOOK')
d = pc.get('ASUS')

PcPrice = { "HP" : 600 , "DELL" : 650 , "MACBOOK" : 1200 , "ASUS" : 400}
A = PcPrice.get('HP')
B = PcPrice.get('DELL')
C = PcPrice.get('MACBOOK')
D = PcPrice.get('ASUS')

print('Total value of available brands:')
print("HP :",a*A)
print("DELL :",b*B)
print("MACBOOK :",c*C)
print("ASUS :",d*D)

total = a*A + b*B + c*C + d*D
print('Total value of available items:', total)
