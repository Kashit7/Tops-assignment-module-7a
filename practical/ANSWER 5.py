''' Write a Python program to find whether a given number is even
or odd, print out an appropriate message to the user.'''

def findEvenOdd(num):
    if(num%2==0):
        print(f"the number {num} is even number")
    else:
         print(f"the number {num} is odd number")


usernumber=int(input("enter you number : "))      
findEvenOdd(usernumber)
        