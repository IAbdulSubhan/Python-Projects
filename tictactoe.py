def sum(x,y,z):
    return x+y+z

def printboard():
    zero  = 'X' if xState[0] else ('O'if zState[0] else 0)
    one  = 'X' if xState[1] else ('O'if zState[1] else 0)
    two  = 'X' if xState[2] else ('O'if zState[2] else 0)
    three  = 'X' if xState[3] else ('O'if zState[3] else 0)
    four  = 'X' if xState[4] else ('O'if zState[4] else 0)
    five  = 'X' if xState[5] else ('O'if zState[5] else 0)
    six  = 'X' if xState[6] else ('O'if zState[6] else 0)
    seven = 'X' if xState[7] else ('O'if zState[7] else 0)
    eight = 'X' if xState[8] else ('O'if zState[8] else 0)
    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")

def print_remaining():
    remaining = [i for i in range(9) if xState[i] == 0 and zState[i] == 0]
    print("Remaining Options:", remaining)

def checkwin(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X wins")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("Z wins")
            return 0
    return -1



if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1  #1 for X and 0 for O
    print("Welcome to tic tac toe")
    while True:
        printboard()
        print_remaining()

        if turn == 1:
            print("X's Turn: ")
            value = int(input("Please enter a value: "))
            if value > 8 or value < 0 or xState[value] == 1 or zState[value] == 1:
                print("Invalid Input")
                continue
            xState[value] = 1
        else:
            print("Z's Turn: ")
            value = int(input("Please enter a value: "))
            if value > 8 or value < 0 or xState[value] == 1 or zState[value] == 1:
                print("Invalid Input")
                continue
            zState[value] = 1

        chk_win = checkwin(xState, zState) 
        if chk_win != -1:
            printboard()
            if chk_win == 0:
                print("X won the match")
                print("Game Over")
                break
            if chk_win == 1:
                print("Z won the match")
                print("Game Over")
                break
            break
        turn = 1 - turn #changig of turns