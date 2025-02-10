'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.'''


def strOpration(str1,str2):
    finalstr=str1+" "+str2
    str2=finalstr.split()
    finalstr2=""
    for i in str2:
        finalstr2+=i[1]+i[0]+i[2:]+" "
    print(finalstr2)

strOpration("hello","world")