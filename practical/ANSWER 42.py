'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
60) Sample string:
'w3resource' Expected output:
• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

str1='w3schooloftech'
dict1={}
for char in str1:  #method 1
    dict1[char]=dict1.get(char,0)+1
    
print(dict1)


dict2={char:str1.count(char) for char in str1} #method 2
print(dict2)
    