'''Write a Python program to map two lists into a dictionary
Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).'''

list_1=['a','b','c','d']
list_2=[400,400,300,400]
dict_1={list_1[i]:list_2[i]for i in range(len(list_1))}
print(dict_1)