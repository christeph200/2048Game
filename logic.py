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


# function to get the current
# state of game
def get_current_state(mat):
 
    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                for row in mat:
                    print(row)
                return 'WON'
 
    # if we are still left with
    # atleast one empty cell
    # game is not yet over
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'
 
    # or if no cell is empty now   
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged they will create an empty
    # cell and in that case game is not yet over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'
    # checking the same for last 2 columns
    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'
    #checking the same for last 2 rows
    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'
 
    # else we have lost the game
    return 'LOST'


# function to compress the grid
# after every step before and
# after merging cells in case of left.
def compress_left(mat):
    # empty grid
    new_mat = []
 
    # intitalise with zero
    for i in range(4):
        new_mat.append([0] * 4)
         
    # here we will shift entries
    # of each cell to it's extreme
    # left row by row
    for i in range(4):
        pos = 0 # to keep track of previous empty cell
 
        # loop to traverse each column
        # in respective row
        for j in range(4):
            if(mat[i][j] != 0): # Check whether the current cell is empty or not
                 
                # if cell is non empty then
                # we will shift it's value to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]
                 
                
                    
                pos += 1 # incrementing to next empty value
 
    # returning new compressed matrix
    return new_mat

# function to compress the grid
# after every step before and
# after merging cells in case of right.
def compress_right(mat):
 
    # bool variable to determine
    # any change happened or not
 
    # empty grid
    new_mat = []
 
    # intitalise with zero
    for i in range(4):
        new_mat.append([0] * 4)
         
    # here we will shift entries
    # of each cell to it's extreme
    # right row by row
    
    for i in range(4):
        pos = 3
 
        # loop to traverse each column
        # in respective row
        for j in range(3,-1,-1): #starting from the end of row as here we deal with right shifting
            if(mat[i][j] != 0):
                 
                # if cell is non empty then
                # we will shift it's value to
                # previous empty cell in that row
                # denoted by pos variable
                new_mat[i][pos] = mat[i][j]
                 
                
                    
                pos -= 1 # decrementing to next empty value
 
    # returning new compressed matrix
    
    return new_mat


def merge_left(mat):
     
    
     
    for i in range(4):
        for j in range(3):
 
            # if current cell has same value as
            # next cell in the row and they
            # are non empty then
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):
 
                # double current cell value and
                # empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
    return mat

# function to merge/add the cells
# in matrix after compressing in case of right
def merge_right(mat):
     
    for i in range(4):
        for j in range(3,0,-1): # start from right
 
            # if current cell has same value as
            # previous cell in the row and they
            # are non empty then
            if(mat[i][j] == mat[i][j - 1] and mat[i][j] != 0):
 
                # double current cell value and
                # empty the previous cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j - 1] = 0
                
 
    return mat

 
# function to get the transpose
# of matrix 
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# function to update the matrix
# if we move / swipe left
def move_left(grid):
 
    # first compress the grid
    new_grid = compress_left(grid)
 
    # then merge the cells.
    new_grid = merge_left(new_grid)
     
    
 
    # again compress after merging.This is done to ensure after addition every element comes to left
    new_grid = compress_left(new_grid)
 
    # return new matrix 
    return new_grid
 
# function to update the matrix
# if we move / swipe right
def move_right(grid):
 
    # first compress the grid
    new_grid = compress_right(grid)
 
    # then merge the cells.
    new_grid = merge_right(new_grid)
     
    
 
    # again compress after merging.This is done to ensure after addition every element comes to right.
    new_grid = compress_right(new_grid)
 
    # return new matrix 
    return new_grid

# function to update the matrix
# if we move / swipe up
def move_up(grid):
 
    # to move up we just take
    # transpose of matrix to make it similar to left
    new_grid = transpose(grid)
 
    # then move left (calling all
    # included functions) then
    new_grid = move_left(new_grid)
 
    # again take transpose so that we can obtain original matrix.
    new_grid = transpose(new_grid)
    return new_grid
 
# function to update the matrix
# if we move / swipe down
def move_down(grid):
 
    # to move down we take transpose to make it similar to right
    new_grid = transpose(grid)
 
    # then move right 
    new_grid = move_right(new_grid)
 
    # again take transpose so that we can obtain original matrix.
    new_grid = transpose(new_grid)
    return new_grid