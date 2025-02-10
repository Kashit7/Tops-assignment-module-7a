'''Write a Python program to find the second smallest number in a list.'''

def second_smallest(lst):
    min_val=lst[0]
    min_valcount=0
    for i in range(1,3):
     for num in lst:
         if num<min_val:
             min_val=num
        
     lst.remove(min_val)
     min_valcount+=1
     if min_valcount != 2:
         min_val=lst[0]
     
    return min_val
    
    
    
    
    
lst=[90,43,55,33,23,11,43,66,77,87,98,9]
print("the second smallest number from list is " , second_smallest(lst))