# Name: Theodoro Gasperin Terra Camargo
# McGill Id: 260842764
#
#  **** N-QUEENS PROBLEM ****
#  
# How many queens on can place on a chess board without them attacking eachother?
# On this assignment I solve this problem using two different approaches. 
# A backtracking approach and a local search one.

from random import randint

def deepcopy(board):
    '''Helper function: makes deep copy of a list'''
    copy = []
    for i in board:
        copy.append(i)
    return copy

def checkAttacks(board):
    '''
    (list) -> list(tuples)
    Helper function: Counts number of attacks between Queens. 
    Possible attacks are btw both diagonals and within the same collum (rows are excluded).
    Returns a list of tuples, where each tuple represents an attack btw two queens. 
    '''
    n = len(board)
    attacks = 0
    conflicts = []

    i = 0
    while i < n:
        j = i + 1
        while j < n:
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

    return conflicts

def createRandomBoard(n):
    '''Helper function: creates a random board.'''
    # Initializing Board
    board = []   
    # Creating broken state/board solution
    for i in range(0, n):   
        board.append(randint(0, n))
    return board
    
# Local Search approach: Hill Climbing
def localSearchQueens(n):
    '''
    (int) -> list
    This function places as many Queens(Q) as possible in a chess board of n x n size. 
    It respect all possible Queen movements constrains not allowing to place a Queen on the same collum, row or both diagonals.
    It uses a local search approach (hill climbing) to solve the N-Queens problem. 
    "board" is an 1D list, where the index of the list represents the row,
    and the list[i] the value of the collum where the queen is located.
    "n" is the size of the board.
    '''

    # Creating initial state
    board = createRandomBoard(n)
    
    attacks = 1         # Heuristic function h(s)  
    while attacks != 0: # while there is attacks btw queens

        neighbor = deepcopy(board)              # Initializing neighbor state/board
        pairsQueen = checkAttacks(board)        # Gets list of pairs of conflicting Queens
        attacks = len(pairsQueen)               # Get n# of attacks by queens
        
        pair = randint(0, attacks - 1)          # Selecting random conflicting pair of queens
        queen = pairsQueen[pair][randint(0,1)]  # Selecting random Queen from the conflicting pair
        
        new_col = randint(0, n-1)                 # Creating a random collum value

        if new_col != board[queen]:             # if new col value != from the current col value
            
            # move conflicting queen to new collum
            neighbor[queen] = new_col           # Creates a neighbor state
            
            # Calculating number of attacks for neighbor state
            attacks1 = len(checkAttacks(neighbor)) 
        else: continue
        
        # if neighbor state has less or equal queens attacking eachother
        if attacks1 <= attacks: 
            board = neighbor                    # Take Greedy Step
            attacks = attacks1                  # Update heuristics h(s)
        else: continue

    return board


# -------- Main --------
def main():
    '''Main'''
    # Length of board. Eg. n = 4
    n = 300 
    
    # Backtracking approach
    #board = [" "]             # Board is 1D list   
    #distributeQueens(board, n)
    
    # Local Search approach
    #printBoard(localSearchQueens(n))
    print(localSearchQueens(n))

if __name__ == "__main__":
    main()
    