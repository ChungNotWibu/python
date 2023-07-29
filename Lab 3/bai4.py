num = int(input("Enter number plz: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by 3 and 5")
else:
    if num % 3 == 0 and num % 5 != 0:
        print(f"{num} is a number that is divisible by 3 but not divisible by 5") 
    else:
        if num % 3 != 0 and num % 5 == 0:
            print(f"{num} is a number that is divisible by 5 but not divisible by 3")
        else:
            print(f"{num} is a number that is not divisible by both 3 and 5")


