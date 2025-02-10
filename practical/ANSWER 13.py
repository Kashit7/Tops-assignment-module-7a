'''Write a Python program to count the occurrences of each word in a
given sentence'''

def findoccurence():
  str1='''Write a Python program to count the occurrences of each word in a
            given sentence'''
  newstr=str1.split()
  occurece=""
  for i in newstr:
      if i not in occurece:
          count=str1.count(i)
          occurece+= i +":"+str(count)+"\n"
  return occurece

print(findoccurence())