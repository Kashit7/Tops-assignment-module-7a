'''Write a Python program to convert a list of characters into a string'''

# def Convert_String(lst): #method 1
#     string=" ".join(lst)
#     return string

def Convert_String(lst): #method 2
    string=" "
    for data in lst:
        if isinstance(data,str):
            string+=data
    return string
        

list1=["a","e","i","o","u"]
print(Convert_String(list1))
print(type(Convert_String(list1)))