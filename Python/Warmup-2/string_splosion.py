#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'


def string_splosion(str):
  result=str[:0]
  a = len(str)
  if len(str) <=1:
    return str
  else:
    for i in range(a+1):
      result = result + str[:i]
    return result
      
