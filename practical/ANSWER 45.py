'''Write a Python function to check whether a number is perfect or not.'''


def num_perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
        sum+=i
  return sum


usernum=int(input("enter a number : "))

if num_perfect(usernum)==usernum:
    print("entered number is a perfect number")
else:
    print("entered number is not a perfect number")
    
    
        
            