'''Write a Python program to select an item randomly from a list.'''

import random

# def Random_Selection(lst): #mathod 1
#     index_no=random.randint(0,len(lst)-1)
#     print(lst[index_no])
    
def Random_Selection(lst): #mathod 2
    random_choice=random.choice(lst)
    print(random_choice)
    
    
    
    
    
    
lst=[1,20,30,40,5,60,7,8,9,"gaurav"]
Random_Selection(lst)