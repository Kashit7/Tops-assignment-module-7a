'''Write a Python program to count occurrences of a substring in a string.'''

def Substroccur(substr):
    str="the cow is animal. and cow gives as milk. cow has four legs"
    newstr=str.split()
    # print(newstr)
    count=0
    for i in newstr:
        if substr==i:
            count+=1
    return count
        
inptstr="cow"
print(f"the count of {inptstr} in str is {Substroccur(inptstr)}")