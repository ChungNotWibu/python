n = int(input("Enter a positive integer: "))
n1 = 1
n2 = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":",n1)
else:
   print(f"First {n} Fibonacci numbers:")
   while count < n:
       print(n1)
       nth = n1 + n2  
       n1 = n2
       n2 = nth
       count += 1   