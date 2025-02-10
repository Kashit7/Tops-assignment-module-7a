'''Write a Python function to reverses a string if its length is a multiple
of 4.'''

def reverseString(str):
    if len(str)%4==0:
        newstr=" ".join(reversed(str))
        return newstr
    else:
        return "the string is not the multiple of 4"
    
result=reverseString("gaur")
print(result)
        