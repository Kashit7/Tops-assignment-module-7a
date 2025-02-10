'''Write a Python program to test whether a passed letter is a vowel
or not.'''

def checkvowel(str):
  vowel="aeiou"
  if str in vowel:
      print(f"the latter {str} is a vowel")
  else:
      print(f"the latter {str} is not a vowel")
      
      
character=input(" enter a latter :  ")
checkvowel(character.lower())
      