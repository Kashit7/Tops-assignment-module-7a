'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.'''

def SumOfThreeValues(val1,val2,val3):
    if(val1==val2 or val2==val3 or val3==val1 ):
        print(f"the sum of these are 0 because two of them are same val1 is {val1} val2 is {val2} val3 is {val3}")
    else:
        return val1+val2+val3
    
num1=int(input("enter first number : "))   
num2=int(input("enter first number : "))   
num3=int(input("enter first number : "))   
print(f'the sum of three inteager are {SumOfThreeValues(num1,num2,num3)}')