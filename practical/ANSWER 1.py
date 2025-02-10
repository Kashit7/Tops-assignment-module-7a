'''Write a Python program to check if a number is positive, negative or
zero.'''

UserNumber=int(input("enter a number you want to check..  "))
FixedValue=0
if(UserNumber!=0):
  if(UserNumber>FixedValue):
      print(f'your number {UserNumber} is Positive number')
  else:
        print(f'your number {UserNumber} is Negative number')
else:
        print(f'your number  is  {UserNumber} ')