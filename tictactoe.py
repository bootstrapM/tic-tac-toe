import itertools
import numpy as np

def diag(game,par):
    lis=[]
    if par==1:
        for i in range(len(game)):
            lis.append(game[i][i])
        return(lis)
    elif par==2:
        for i in range(len(game)):
            lis.append(game[i][len(game)-1-i])
        return(lis)

def win(game):
    def all_same(param, wintype):
        if param.count(param[0]) == len(param) and param[0] != 0:
            print(f"winner is player {param[0]}: "+ "wintype = "+wintype)
            return(True)
        return(False)
    
    for row in game:
        if all_same(row, "horizontally") == True:
            return(True)

    for col in list(map(list,zip(*game))):
        if all_same(col, "vertically") == True:
            return(True)

    if all_same(diag(game,1), "diagonally") == True:
        return(True)

    if all_same(diag(game,2), "anti-diagonally") ==True:
        return(True)
    return(False)

def draw(game):
    if win(game) == False and np.prod(list(itertools.chain(*game))) != 0:
        print("draw!")
        return(True)
    return(False)


def game_board(game, game_size = 3, row_pos = 0, col_pos = 0, curr_player = 0):
    if game[row_pos][col_pos] != 0:
        print("position occupied! Try again")
        return(False, game)
    if curr_player != 0:
        game[row_pos][col_pos] = curr_player

    st = "   "+"  ".join(list(map(str,list(range(game_size)))))
    print(st)
    for row, col in enumerate(game):
        print(row,col)
    return(True, game)

terminate_program = False
while not terminate_program:
    game_size = int(input("What size game board do you want to play on? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_board(game, game_size, 0 , 0 , 0)

    game_play = False
    temp = itertools.cycle([1,2])
    while not game_play:
        curr_player = next(temp)
        attempt = False
        while not attempt == True:
            print(f"player {curr_player} move")
            row_pos = int(input("enter the row position "))
            col_pos = int(input("enter the column position "))
            curr_board = game_board(game, game_size,row_pos,col_pos,curr_player)
            if curr_board[0] == True:
                attempt = True
        if curr_board[0] == True:
            if win(curr_board[1]) == True or draw(curr_board[1]) == True:
                game_play = True
                again = input("Would you like to play again? (y/n) ")
                if again.lower() == "n":
                    print("Bye bye")
                    terminate_program = True;
                else:
                    print("Restarting the game ...")
                    






