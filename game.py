import logic


# Driver code
if __name__ == '__main__':
     
# calling start_game function
# to initialize the matrix
    mat = logic.start_game()
 
while(True):
    for row in mat:
        print(row)
        
    # taking the user input
    # for next step
    x = input("Press the command : ")
 
    # we have to move up
    if(x == '3'):
 
        # call the move_up function
        mat  = logic.move_up(mat)
 
        # get the current state and print it
        status = logic.get_current_state(mat)
        print(status)
 
        # if game not over then continue
        # and add a new two
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
 
        # else break the loop
        else:
            
            break
 
    # the above process will be followed
    # in case of each type of move
    # below
 
    # to move down
    elif(x == '4'):
        mat = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
 
    # to move left
    elif(x == '1'):
        mat = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
 
    # to move right
    elif(x == '2'):
        mat = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    else:
        print("Invalid Key Pressed")
 