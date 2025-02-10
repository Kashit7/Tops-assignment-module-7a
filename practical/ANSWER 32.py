'''Write a Python program to unzip a list of tuples into individual lists'''

# def unzip_tuple(lst): #mathod 1
#     for i in range(len(lst)):
#         lst[i]=list(lst[i])
        
#     lst1,lst2,lst3=lst
#     return lst1,lst2,lst3

def unzip_tuple(lst): #mathod 2
    rest1,rest2,rest3=map(list, lst)
    return rest1,rest2,rest3               # for lst in map(list,lst):
                                           #     print(lst)
    


        
    
list1=[(1,2,3),(2,4,8),(3,6,9)]
res1,res2,res3=unzip_tuple(list1)
print(res1,"\n",res2,"\n",res3)