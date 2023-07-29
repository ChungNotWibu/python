# === Bài 3 ===
num = int(input("Enter a number: "))
a = 1
if num >= 0:
    for i in range(1,num +1):
        a = a*i
    print(f"Factorial of {num} is:" , a)
else:
    print("In va lít năm bờ!!!")