def FirstFactorial(num): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  if num == 0:
    return 1
  else:
    return num * FirstFactorial(num - 1)
    
# keep this function call here  
print FirstFactorial(raw_input())  
