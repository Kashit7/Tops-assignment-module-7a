'''Write a Python program to remove duplicates from a list.'''

def removeDuplicate(lst):
    var_unique=[]
    for data in lst:
        if data not in var_unique:
            var_unique.append(data)
        else:
            print(data,end=" ""is duplicate value ,")
    return var_unique

lst=[12,32,12,54,65,45,54,99,100,98,99]
print("\n",removeDuplicate(lst))