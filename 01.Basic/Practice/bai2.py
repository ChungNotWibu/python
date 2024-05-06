import math

print("equation")
a = int(input("Enter a plz: "))
b = int(input("Enter b plz: "))
c = int(input("Enter c plz: "))

while True: 
    if a == 0 and b == 0 :
        print("One of the numbers a and b must be different from 0")
        print('Enter a again plz')
        a = int(input("Number a :"))
        print('Enter b again plz')
        b = int(input("Number b :"))
    else:
        break

delta = b**2 - 4*a*c

if delta < 0  :
    print("The equation has no solution!")
elif delta == 0 :
    print("The equation has a double solution :" , -(b / (2 * a)))
else:
    print("The equation has two distinct solutions")
    print("x1 :", (-(b) + math.sqrt(delta))/(2*a))
    print("x2 :", (-(b) - math.sqrt(delta))/(2*a))

