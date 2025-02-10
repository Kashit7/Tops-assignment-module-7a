'''Write a Python script to sort (ascending and descending) a
dictionary by value.'''

dict1={
    "KASHIT":2,
    "YASH":1,
    "MEET":3
}

res=dict(sorted(dict1.items(),key=lambda x:x[1]))
print(res)