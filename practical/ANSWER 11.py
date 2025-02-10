'''Write a Python program to count the number of characters
(character frequency) in a string'''

def characterfrequency(string):
    freq = ""

    for char in string:
        if char not in freq:
            count = string.count(char)
            freq += char +":"+ str(count)+"\n"

    return freq

inputstring = "gaurav goswami"
result = characterfrequency(inputstring)
print(result)