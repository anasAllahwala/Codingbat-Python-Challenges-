
#Given a string, return a string where for every char in the original, there are two chars.

#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  result =""
  a = len(str)
  for i in range(a):
    result = result + str[i] + str[i]
  return result
