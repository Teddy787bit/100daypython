def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if not wall_on_right():
        jump()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()  
    else:
        move()

