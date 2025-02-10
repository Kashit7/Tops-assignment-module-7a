'''Write a Python script to concatenate following dictionaries to create
a new one.'''

dict1={
    1:"DABELI",
    2:"FRIES",
    3:"PUFF"
    
}
dict2={
    4:"COKE",
    5:"THUMBSUP",
    6:"LEMON SODA"
    
}

dict3=dict1
# dict3=dict1 #mathod 1
# for i,j in dict2.items():
#     dict3.update({i:j})
# print(dict3)   

dict3={**dict1,**dict2} 
print(dict3)