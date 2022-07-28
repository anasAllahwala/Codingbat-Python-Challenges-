#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False


def near_hundred(a):
  diff = 100 - a
  if abs(diff) <=10:
    return True 
  diff = 200 - a
  if abs(diff) <=10:
    return True
  else:
    return False
