'''Write a Python program to get the Fibonacci series of given range.'''

def fibonacci(n):
    if n==0 or n==1:
        return n
    a=0
    b=1
    count=0
    print(a,b,end=" ")
    while(count<n-2):
      c=a+b
      a,b=b,c
      print(c,end=" ")
      count+=1
     
fibonacci(5)