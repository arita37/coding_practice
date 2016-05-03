def LetterCapitalize(str): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  words = [word[0].capitalize()+word[1:] for word in str.split()]
  str = " ".join(words)
  return str    
    
# keep this function call here  
print LetterCapitalize(raw_input())
