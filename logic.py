# logic.py to be
# imported in the game.py file
 
# importing random to get random numbers
import random
 
# function to start a game
def start_game():
 
    # initialising board with zeroes
    mat =[]
    for i in range(4):
        mat.append([0] * 4)
 
    # printing controls for user
    print("Commands are as follows : ")
    print("1 : Move Left")
    print("2 : Move Right")
    print("3 : Move Up")
    print("4 : Move Down")
 
    # calling the function to add
    # 2 or 4 in the grid after every step
    add_new_2(mat) # Called 2 times intitally
    add_new_2(mat)
    return mat
 
# function to add a new 2 or 4 in
# grid at any random empty cell
def add_new_2(mat):
 
   # choosing a random row and column index
   
    r = random.randint(0, 3)
    c = random.randint(0, 3)
 
    # loop until it finds a random cell with value zero in the grid
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
 
    # we will place a 2 or 4 at that empty
    # random cell.
    l=[2,4]
    mat[r][c] = random.choice(l)