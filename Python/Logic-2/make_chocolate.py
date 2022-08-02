#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming 
#we always use big bars before small bars. Return -1 if it can't be done.

#make_chocolate(4, 1, 9) → 4
#make_chocolate(4, 1, 10) → -1
#make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
  diff = goal
  if (big*5 + small) <goal:
    return -1 
  if goal ==5 and big>=1:
    return 0
  if goal<5 and small >=goal:
    return goal
  if big*5>goal:
    while(diff>5):
      big = big-1
      diff = diff -5
      if diff<5 and small >=diff:
        return diff
    return -1
  if big*5 + small>=goal and  big*5<goal:
    diff = goal - big*5
    return diff
  if big*5==goal:
    return 0
 
 
  
  
    
    

    
        
    
      
      
      
      
      
  
