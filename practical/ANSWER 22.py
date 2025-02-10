'''Write a Python program to check a list is empty or not.'''

def Checklist_Empty(lst):
    # if lst==[]:
    #     print("the list is empty")
    # else:
    #     print('the list is not empty')
    if bool(lst):
        print("the list is not empty")
    else:
        print('the list is empty')


lst=[1,3]
Checklist_Empty(lst)        