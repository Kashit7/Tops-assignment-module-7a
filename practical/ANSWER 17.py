'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''

def getnewStr(str):
    if len(str)>2:
      newstr=str[0:2]+str[-2:]
      return newstr
    else:
        return " "
    

result=getnewStr("KASHIT")
print(result)
    