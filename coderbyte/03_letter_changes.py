def LetterChanges(str): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  outstr = ''
  for char in str:
    if char.isalpha():
      newchar = chr(ord(char) + 1)
      if newchar in ['a','e','i','o','u']:
        newchar = newchar.capitalize()
      outstr += newchar
    else:
      outstr += char
      
  return outstr
    
# keep this function call here  
print LetterChanges(raw_input())  
