s = input("Enter some thing:")

def isPalindrome(s):
    return s == s[::-1] 
ans = isPalindrome(s)

if ans:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")  