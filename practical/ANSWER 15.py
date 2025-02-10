'''Write a Python program to add 'in' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then
add 'ly' instead if the string length of the given string is less than 3,
leave it unchanged.'''

def stringConditions(str):
    if len(str)>=3:
        if str.endswith("ing"):
            nstr=str.replace('ing', 'ly')
            return nstr
        else:
            newstr=str+'ing'
            return newstr
    else:
        return str
    
result=stringConditions("gaing")
print(result)