'''Write a Python program that will return true if the two given
integer values are equal or their sum or difference is 5.'''

def CheckConditions(a,b):
    if(a==b or a+b==5 or a-b==5):
        return True
    else:
        return False
    
    
num1=int(input("enter first number : "))
num2=int(input("enter first number : "))
print(CheckConditions(num1,num2))