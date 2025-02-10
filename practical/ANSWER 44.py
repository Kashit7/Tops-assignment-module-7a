'''Write a Python function to check whether a number is in a given range'''

def func_in_range(n):
    start=36
    end=88
    if n>=start and n<=end:
        return"the given number in range"
    else:
        return"the given number is not in range"
    
userinput=int(input("enter a number between 36 and 88 : "))
print(func_in_range(userinput))