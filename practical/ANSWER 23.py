'''Write a Python function that takes two lists and returns true if they
have at least one common member.'''


def Check_Common(lst1,lst2):
    for data in lst1:
        if data in lst2:
            return True
        
            
        
        
lst1=[1,2,3,4,3,4]
lst2=[6,7,8,9,7,3]
if Check_Common(lst1,lst2):
    print("there are some common elemnts")
else:
    print("there are no common element")