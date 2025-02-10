'''Write a Python function to calculate the factorial of a number (a
nonnegative integer)'''

def factorial(n):
    if n>0:
        if n==1:
            return n
        return factorial(n-1)*n

print(f'tha fact is {factorial(4)}')
    

        