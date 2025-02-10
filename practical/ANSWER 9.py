'''Write a python program to sum of the first n positive integers.'''

def SumofPositivenum(num):
    result=0
    if num>0:
     for i in range(1,num+1):
        result+=i
    else:
        print("please enter positive number")
        
    return result

usernumber=int(input("enter first n positive number you want to sum : "))
print(f"the sum of first {usernumber} is number {SumofPositivenum(usernumber)}")
        