'''Write a Python function to insert a string in the middle of a string.'''

def insertString(str,str2):
    midstr=len(str)//2
    newstr=str[0:midstr]+str2+str[midstr:]
    return newstr


original="gaurav"
addstr="the"
print(insertString(original,addstr))