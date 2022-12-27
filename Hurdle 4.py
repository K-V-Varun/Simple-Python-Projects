def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right()==True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear()==True:
        move()
    turn_left()
  
while at_goal()==False:
    if front_is_clear()==True:
        move()
    elif wall_in_front()==True:
        jump()

    
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
