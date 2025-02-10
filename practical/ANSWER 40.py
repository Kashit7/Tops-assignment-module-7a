'''Write a Python program to find the highest 3 values in a dictionary'''

dict_1={
    "eng": 91,
    "math" : 46,
    "phy": 58,
    "guj": 98,
    "chem": 39,
    "SS":78
    
}
number=sorted(dict_1.items(),key=lambda x:x[1],reverse=True)
print(number[:3])
    