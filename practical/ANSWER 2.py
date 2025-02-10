'''Write a Python program to get the Factorial number of given numbers.'''

# Number=int(input("enter a number for a factorial you want..")) #mathod 1
# result=1
# for i in range(1,yourNumber+1):
#     result*=i
# print(result)
 
Number=int(input("enter a number for a factorial you want.."))
check=1
result=1
while(check<=Number):
    result*=check
    check+=1
print(f'this is your answer for the factorial {Number}  : ' , result)