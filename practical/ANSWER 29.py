'''Write a Python program to check whether a list contains a sub list'''

def check_sublist(lst,lst2):
    sub_listlen=len(lst2)
    for i in range(len(lst)-(sub_listlen-1)):
        if lst[i:i+sub_listlen]==lst2:
            print("list contain sublist")
            break
            
            
list1=[1,2,3,4,56,6,4,56,78,98,43,5]
list2=[4,56,78,98]
check_sublist(list1,list2)