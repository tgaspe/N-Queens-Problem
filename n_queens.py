# Name: Theodoro Gasperin Terra Camargo
# McGill Id: 260842764
#
#  **** N-QUEENS PROBLEM ****
#

from random import randint

def deepcopy(board):
    '''Helper function: makes deep copy of list'''
    copy = []
    for i in board:
        copy.append(i)
    return copy

def checkAttacks(board):
    '''
    (list) -> int
    Helper function: Counts number of attacks between Queens
    '''
    n = len(board)
    attacks = 0
    conflicts = []


    i = 1
    while i < n:
        #print(str(i) + " ------")
        j = i + 1
        while j < n:
            #print("j " + str(j) + " => board[i] " + str(board[i]) + " board[j] " + str(board[j]))
            pair = (i, j)
            
            if   board[i] == board[j]:         # there is a Q already at the same collum on row level i
                conflicts.append(pair)
                attacks += 1   
            elif board[i] == board[j] + j - i: # there is a Q already at the right ( / ) diagonal on row level i
                conflicts.append(pair)
                attacks += 1       
            elif board[i] == board[j] - j + i: # there is a Q already at the left  ( \ ) diagonal on row level i
                conflicts.append(pair)
                attacks += 1      
            j += 1
        i += 1
    #print("attacks: " + str(attacks))
    #print(conflicts)
    return conflicts

def createRandomBoard(n):
    board = ["#"]   # Initializing Board
    for i in range(1, n + 1):   # Creating broken state solution
        board.append(randint(1, n))
    return board
    

def localSearchQueens(n):
    '''Definition'''

    board = createRandomBoard(n)
    
    attacks = 1         # Heuristic function initialization  
    while attacks != 0: # while there is attacks btw queens

        neighbor = deepcopy(board)      # Initializing neighbor state board
        pairsQueen = checkAttacks(board)# Gets list of pairs of conflicting Queens
        attacks = len(pairsQueen)       # Get n# of attacks by queens
        
        pair = randint(0, attacks - 1)  # Selectin random conflicting pair of queens
        queen = pairsQueen[pair][randint(0,1)]     # Selecting random Queen from the conflicting pair
        
        #print("\nBoard " + str(board))
        #print("p attacks: " + str(attacks))
        #print("List conflicts " + str(pairsQueen))
        #print("pair: " + str(pair))
        #print("queen: " + str(queen))

        
        new_col = randint(1, n)

        if new_col != board[queen]:     # if new col value different form the current col value
            #print("new-col: " + str(new_col))
            neighbor[queen] = new_col   # moving conflicting queen to new collum
            attacks1 = len(checkAttacks(neighbor)) # Calculating number of attacks for neighbor state
            #print("attacks1 " + str(attacks1))
            #print("neighbor: " + str(neighbor))

        else: continue
        
        
        if attacks1 <= attacks: # if neighbor state has less or equal queens attacking eachother
            board = neighbor
            attacks = attacks1
        else: continue


    return board[1:]



#print("\nResult: " + str(localSearchQueens(8)))




#checkAttacks(["#", 1,2,3, 4])


# Constructive Approach: Backtracking Search
def distributeQueens(board, n, row = 1):
    '''
    (list, int, int) -> str
    This function places as many Queens(Q) as possible in a chess board of n x n size. 
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




def printBoard(board):
    '''Helper function: prints 2d board'''
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
    #board = [" "]       # Board is 1D list where the index represents the row and the board[i] the collum where the Queen resides 
    n = 8               # Length of board. Eg. n = 4
    #distributeQueens(board, n)
    printBoard(localSearchQueens(n))
    

if __name__ == "__main__":
    main()
    