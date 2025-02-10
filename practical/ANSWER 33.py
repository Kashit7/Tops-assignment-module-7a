'''Write a Python program to convert a list of tuples into a dictionary.'''

# def lstOfTupleIntoDict(lst): #mathod 1
#     return dict(lst)
# list1=[(1,"gaurav"),(2,"shivam"),(3,"aniket")]
# print(lstOfTupleIntoDict(list1))

def lstOfTupleIntoDictTwo(lst): #mathod 2
    finalOutPut={data[0]:(data[1],data[2])for data in lst} #dict compreh..
    return finalOutPut
    

list2=[(1,3,"gaurav"),(2,4,"shivam"),(3,5,"aniket")]
print(lstOfTupleIntoDictTwo(list2))