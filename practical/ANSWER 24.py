'''Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.'''

def List_Oprations():
    new_lst=[i**2 for i in range(1,31)]
    print(new_lst[:5])
    print(new_lst[-5:])
    
    
List_Oprations()
    