# boardsolver.py
def solve(board):
    """
    This is a program that finds a possible
    solution using backtracking algorithm

    It goes through all possible solutions and finds
    the correct one
    """
    find = if_empty(board) #this finds the next unfilled block and returns its coordinates
    if find:
        row, col = find
    else:
        return True #If nothing is found we come to a solution

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0 # This is for backtracking if the solution previously made was incorrect

    return False


def valid(board, pos, num):
    """
    This tells if the attempted number at the position is valid or not
    """

    # Checking the row if any of the number in it is same as the one we choose
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Similarly, checking the column if it is previously there on the column or not
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Checking the 3X3 box if there is some number previously which is same as the one we choose

    box_x = pos[1]//3 # Starting ordinate of the box to where the current position belongs
    box_y = pos[0]//3 # Similarly, this is the abscissa

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True #we retutn true if none of the numbers are same in row, column and in the box containing the position


def if_empty(board):
    """
    It returns the coordinate of a point whose value is zero
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None # Returns nothing if board is full


def print_board(board):
    """
    This is to output the board
    how it looks 
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")

