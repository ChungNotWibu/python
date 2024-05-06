s = input("Enter some thing:")
def isPalindrome(s):
    return s == s[::-1] 
ans = isPalindrome(s)
if ans:
    print("True")
else:
    print("False")