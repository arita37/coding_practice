def LongestWord(sen): 

  # code goes here 
  # Note: don't forget to properly indent in Python
  words = sen.split()
  lengths = [sum(1 for i in word if i.isalpha()) for word in words]
  idx_max_length = lengths.index(max(lengths))
  return words[idx_max_length]
    
# keep this function call here  
print LongestWord(raw_input())
