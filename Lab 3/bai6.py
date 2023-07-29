a = int(input("Enter side length a :"))
b = int(input("Enter side length b :"))
c = int(input("Enter side length c :"))
if a < 0 and b < 0 and c < 0:
    print("Enter a positive numbers")
else:
    if (a + b > c) and (a + c > b) and (b + c > a) :
        print ("All 3 numbers are sides of a triangle")
    else :
        print("All 3 numbers are not sides of a triangle")