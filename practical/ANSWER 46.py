'''Write a Python function that checks whether a passed string is
palindrome or not'''


def palindrome(str1):
    if str1==str1[::-1]:
        print("the string is palindrome")
    else:
        print("the string is not a palindrome")
        
userstr=input("enter your str : ")
palindrome(userstr)
    