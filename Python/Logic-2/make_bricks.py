#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True
#if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. 
#See also: Introduction to MakeBricks


#make_bricks(3, 1, 8) → True
#make_bricks(3, 1, 9) → False
#make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  diff = goal
  if (big*5 + small) <goal:
    return False 
  if goal ==5 and big>=1:
    return True
  if goal<5 and small >=goal:
    return True
  if big*5>goal and (goal%5)==0:
    return True
  if big*5>goal:
    while(diff>5):
      big = big-1
      diff = diff -5
      if diff<5 and small >=diff:
        return True
    return False
  if big*5 + small>=goal and  big*5<goal:
    diff = goal - big*5
    return True
  if big*5==goal:
    return True
 
