#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, 
#round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c,
#return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. 
#Write the helper entirely below and at the same indent level as round_sum().

#round_sum(16, 17, 18) → 60
#round_sum(12, 13, 14) → 30
#round_sum(6, 4, 4) → 10

def round10(num):
    if num<10:
     if num>5 or num==5:
      num = 10
     else:
       num =0
    else:
     a = num%10
     b = num/10
     if a<5:
       while(a!=0):
         num = num -1
         a=num%10
     else:
       while(a!=0):
         num = num+1
         a=num%10
    return num
def round_sum(a, b, c):
  a1=round10(a)
  a2=round10(b)
  a3=round10(c)
  
  return a1+a2+a3
    
