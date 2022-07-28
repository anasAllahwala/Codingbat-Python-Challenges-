#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  a = len(str)
  if a <=1:
    return str
  else:
      return str[a-1:]+ str[1:-1]    + str[:a-a+1] 
