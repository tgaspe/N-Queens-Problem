# Name: Theodoro Gasperin Terra Camargo
# McGill Id: 260842764
#
#  **** N-QUEENS PROBLEM ****
#

def distributeQueens(board, n, row=1):
    '''
    (list, int, int) -> str
    This function places as many Queens as possible in a chess board of n x n size. 
    It respect all possible Queen movements constrains not allowing to place a Queen on the same collum, row or both diagonals.
    It uses recursion to explore the state tree, and prints the final chess board as the result. 
    "board" is an 1D list, "row" is an int representing the current row in the recursion,
    "n" is the size of the board 
    '''

    if row == n + 1: # if row is one unit bigger than board size print board
        print("\nBoard: " + str(board[1:]))
        printBoard(board[1:])
    
    else:
        for j in range(1, n + 1): # Looping through collums ( 1 ... n ) at row level
            legal = True # Legal placement of Q
            
            for i in range(1, row):  # Checks for Q placement accounting for the queens already on rows 1 through r-1
                if   board[i] == j: legal = False               # there is a Q already at the same collum on row level i
                elif board[i] == j + row - i: legal = False     # there is a Q already at the right ( / ) diagonal on row level i
                elif board[i] == j - row + i: legal = False     # there is a Q already at the left  ( \ ) diagonal on row level i
            
            if legal:
                board1 = deepcopy(board)
                board1.insert(row, j) # Adding Queen to board
                distributeQueens(board1, n, row + 1)


def deepcopy(board):
    '''Helper function makes deep copy of list'''
    copy = []
    for i in board:
        copy.append(i)
    return copy

def printBoard(board):
    '''Helper function prints 2d board'''
    board_2d = []
    for j in range(len(board)): # loop through rows
        row = []
        for l in range(len(board)): # loop through cols
            row.append("=")
        board_2d.append(row)
        
        index = 0
        for q in board:
            if index == j:
                row[q-1] = "Q"
            index += 1
        print(row)

def main():
    '''Main'''
    board = [" "]       # Board is 1D list where the index represents the row and the board[i] the collum where the Queen resides 
    n = 4               # Length of board. Eg: 
    distributeQueens(board, n)

if __name__ == "__main__":
    main()
    