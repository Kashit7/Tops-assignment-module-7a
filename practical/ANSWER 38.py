'''Write a Python program to check multiple keys exists in a dictionary'''


def ceckMultipleKey(dictnr,keys):
    dict_keys=dictnr.keys()
    if list(dict_keys)==keys:
        print("all the keys are available in dict")
    else:
        print("all the keys are not in dict")
    
    
    
    
    
    



dictnr={
    "name" : "KASHIT",
    "age" : 17,
    "class" : 11
}

list_of_key=["name","age","KASHIT"]

ceckMultipleKey(dictnr,list_of_key)