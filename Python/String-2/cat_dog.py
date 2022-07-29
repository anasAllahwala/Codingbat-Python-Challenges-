#Return True if the string "cat" and "dog" appear the same number of times in the given string.

#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True

def cat_dog(str):
  count_c =0
  count_d=0
  
  for i in range(len(str)):
    if str[i:i+3] == "cat":
      count_c = count_c+1
    elif str[i:i+3] == "dog":
      count_d = count_d+1
    
  if count_c==count_d:
    return True
  else:
    return False
