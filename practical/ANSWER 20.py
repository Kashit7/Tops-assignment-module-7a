'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list
of strings.'''

def countString(lst):
    count=0
    for data in lst:
        if type(data)==str and len(data)>=2 and data[0]==data[-1]:
            print(data)
            
lst1=[54,"gag",78]
countString(lst1)