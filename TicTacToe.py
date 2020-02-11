# Author: Anthony Ferrari
# Date: 02/11/20


board = [['' for x in range(3)] for y in range(3)]
ai = 'O'
human = 'X'


def print_board(board):
    """Function to print out game board
    :param board: An empty board framework"""

    for row in range(3):
        if row != 0:
            print("- - - - - -")
        for col in range(3):
            if col != 0:
                print('| ', end=" ")
            if col == 2:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end=" ")


def playerMove():
    """Function that allows for player to make a move"""

    run = True
    while run:
        move = input('Please select a row position to place an X in range 1-3')
        move1 = input('Please select a column position to place an X in range 1-3')
        try:
            move = int(move)
            move1 = int(move1)
            if move in range(4) and move1 in range(4):
                if spaceIsFree(move, move1):
                    run = False
                    addPlayerMove(move, move1, human)
                else:
                    print('This space is already occupied. Please choose another. ')
            else:
                print("This number is not in the range. Please a new number")
        except:
            print('You did not type in a number. Please type a number')


# helper function
def addPlayerMove(row, column, player):
    """Updates the index in the board to the player move and returns True
    :param row: row of the board
    :param column: column of the board
    :param player: variable that could be human or ai"""

    board[row][column] = player
    return True


# checks to see if there is free space
def spaceIsFree(row, column):
    """Checks if the index referenced is an empty string and returns True if it is
    :param row: row of the board
    :param column: column of the board"""

    if board[row][column] == '':
        return True
    else:
        return False


# checks to see if there is a winner
def isWinner(player):
    """Checks different combinations of indices on the board to see if a player has won
    and returns True if they have else it returns False"""
    winner = None
    if (board[0][0] == player and board[1][0] == player and board[2][0] == player or
            board[0][0] == player and board[0][1] == player and board[0][2] == player or
            board[1][0] == player and board[1][1] == player and board[1][2] == player or
            board[2][0] == player and board[2][1] == player and board[2][2] == player or
            board[0][1] == player and board[1][1] == player and board[2][1] == player or
            board[0][2] == player and board[1][2] == player and board[2][2] == player or
            board[0][0] == player and board[1][1] == player and board[2][2] == player or
            board[0][2] == player and board[1][1] == player and board[2][0] == player):
        if player == ai:
            return 'X'
        else:
            return 'O'
    else:
        if winner is None and board.count('') == 10:
            return 'DRAW'


# checks to see if the board is full
def isBoardFull():
    if board.count('') > 1:
        return True
    else:
        return False


# computer move
def compMove():
    """Function for ai to play it's optimal move"""

    return addPlayerMove(bestMove()[0], bestMove()[1], ai)


def bestMove():
    """Function that calculates the best move to take based off the best score returned from minimax"""
    # AI to make its turn
    best_score = float("-inf")
    move = (0,0)
    for row in range(3):
        for column in range(3):
            if spaceIsFree(row, column):
                addPlayerMove(row, column, ai)
                score = minimax(board, 0, False)
                addPlayerMove(row, column, '')
                if score > best_score:
                    best_score = score
                    move = (row, column)
                    return move
    else:
        return move


scores = {'X': 10, 'O': -10, 'DRAW': 0}


# minimax algorithm
def minimax(board, depth, isMaximizing):
    """Function that calculates the best score recursively using depth first search
    :param board: game board
    :param depth: levels in the tree
    :param isMaximizing: boolean condition to check optimal move for both ai and human"""
    results = isWinner(ai)
    if results is not None:
        return scores[results]
    if isMaximizing:
        best_score = float('-inf')
        for row in range(3):
            for column in range(3):
                if spaceIsFree(row, column):
                    board[row][column] = ai
                    score = minimax(board, depth + 1, False)
                    board[row][column] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for column in range(3):
                if spaceIsFree(row, column):
                    board[row][column] = human
                    score = minimax(board, depth - 1, True)
                    board[row][column] = ''
                    best_score = min(score, best_score)
        return best_score


def main():
    """Function that allows for game play to occur"""

    print("Welcome to the game, player one!")
    print_board(board)

    while not isBoardFull():  # while board is not full
        if not (isWinner(ai)):
            playerMove()
            print_board(board)
        else:
            print("The AI won!")
            break

        if not (isWinner(human)):
            if isBoardFull():
                print("It's a tie game")
            else:
                move = compMove()
                print('Computer placed an O')
                print_board(board)
        else:
            print("You won this time, good job!")
            break
    if isBoardFull():
        print('TIE GAME')


print_board(board)
main()
# testing code below:
#
# tic = TicTacToe()
# print(tic._count)
# tic.make_move(0,0,'o')
# #print(tic._count)
# tic.make_move(0,1,'o')
# #tic.make_move(1,0,'o')
# tic.make_move(2,0,'o')
# print(tic.get_current_state())
# tic.make_move(0,2,'x')
# tic.make_move(1,2,'o')
# tic.make_move(2,2,'x')
# tic.make_move(1,0,'x')
# tic.make_move(2,1,'x')
# tic.make_move(1,1,'o')
# #print(tic._count)
# print(tic.get_current_state())
# # tic.make_move(0,1,'x')
# # print(tic.get_current_state())


# tic.draw_board()
