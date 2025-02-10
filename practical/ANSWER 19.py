'''Write a Python function to get the largest number, smallest num
and sum of all from a list.'''

# def listopration(lst): #mathod num 1
#     lst.sort()
#     sum=0
#     for i in lst:
#         sum+=i
        
#     return f'the sum of list is {sum} and the largest num is {lst[len(lst)-1]} and the smallest num is {lst[0]}'



def listopration(lst): #mathod num 2
    sum=0
    min_value=lst[0]
    max_value=lst[0]
    for i in lst:
        sum+=i
        if i < min_value:
            min_value=i
        elif i>max_value:
            max_value=i
    return f'the sum of list is {sum} and the largest num is {max_value} and the smallest num is {min_value}'



orgnlst=[12,32,45,64,76,34,98,12,43,56,87]
print(listopration(orgnlst))
        
    