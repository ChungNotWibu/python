a = int(input("Enter side length a :"))
b = int(input("Enter side length b :"))
c = int(input("Enter side length c :"))
if a < 0 and b < 0 and c < 0:
    print("Enter a positive numbers")
else:
    if (a + b > c) and (a + c > b) and (b + c > a) :
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a :
            print("All 3 numbers are sides of a right triangle")
        elif a == b and b == c :
            print("All 3 numbers are sides of an equilateral triangle")
        else:
            print ("All 3 numbers are sides of a triangle")
    else:
        print("All 3 numbers are not sides of a triangle")