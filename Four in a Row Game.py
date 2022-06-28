import time  # ALLOW THE PRINT STATEMENTS TO WAIT A SECOND OR TWO BEFORE PRINTING, OR IN OTHER WORDS, USE THE FUNCTION SLEEP
p1 = input("Player X enter your name: ")  # GET THE PLAYERS' NAMES
p2 = input("Player O enter your name: ")
time.sleep(1) 
print("This is a game of Connecting Dots.") 
time.sleep(1)
print("Try to get 4 in a row")
time.sleep(1)
print("Let's get started!") 
time.sleep(1)  # IN THE NEXT LINE, THAT IS THE GAME BOARD. I USED NESTED LISTS, LISTS WITHIN LISTS
board = [['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
def check_horizontal_win(): # CHECK FOR A HORIZONTAL WIN, FOUR IN A ROW
    for row in range(0,6):
        for col in range(0,4):
            if (board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]=='X') or (board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]=='O'):
                return True
    return False

def check_vertical_win():  # CHECK FOR A VERTICAL WIN
    for i in range(0,7):  # I USED i AND l BECAUSE THEY ARE SHORT. l IS THE ROW, i IS THE COLUMN
        for l in range(0,3):
            if (board[l][i]==board[l+1][i]==board[l+2][i]==board[l+3][i]=='X') or (board[l][i]==board[l+1][i]==board[l+2][i]==board[l+3][i]=='O'):
                return True
    return False

def check_diagonal_win(): # CHECK FOR A DIAGONAL WIN
    for i in range(0,2): # CHECKS DIAGONAL COLUMNS, starts bottom, up to the right, DOESN'T INCLUDE ONE POSSIBLILITY, I'LL COVER IT LATER(don't worry, I'm double sure it's only one:)
        for l in range(0,3): # i is the row, l is the column, 
            if (board[i][l]==board[i+1][l+1]==board[i+2][l+2]==board[i+3][l+3]=='X') or (board[i][l]==board[i+1][l+1]==board[i+2][l+2]==board[i+3][l+3]=='O'):
                return True
    for i in range(0,2): # BOTTOM RIGHT TO TOP LEFT... ALL POSSIBILITIES COVERED
        for l in range(3,7):
            if (board[i][l]==board[i+1][l-1]==board[i+2][l-2]==board[i+3][l-3]=='X') or (board[i][l]==board[i+1][l-1]==board[i+2][l-2]==board[i+3][l-3]=='O'):
                return True
    for i in range(3,6): # Checks the last possibility of bottom left to top right, turns out I made a number one less than it should be
        for l in range(3,7):
            if (board[i][l]==board[i-1][l-1]==board[i-2][l-2]==board[i-3][l-3]=='X') or (board[i][l]==board[i-1][l-1]==board[i-2][l-2]==board[i-3][l-3]=='O'):
                return True
    return False

print('')   # THIS, AND THE NEXT FOUR LINES IS FOR PRINTING THE BOARD
print('0 1 2 3 4 5 6')
for i in board:
    print(" ".join(i))
print('')

for i in range(0,42):  # THE NUMBER 42 IS RANDOM, IT'S JUST SO THERE IS A LOOP, I WAS GOING TO MAKE A WHILE LOOP, BUT I DID THE FUNCTIONS CHECK_HORIZONTAL_WIN AND THE OTHER FUNCTIONS INSTEAD.
    if board[0][0]==board[0][1]=='T': # THIS LINE IS COMPLETELY RANDOM, I JUST DIDN'T WANT TO TAKE AWAY ALL THE TABS IN THE NEXT LINES. DON'T TYPE T.
        break
    else:
        c1 = input(str(p1)+", your token is X. What column do you want to play in? ")  # FIRST PLAYER'S TURN, NOW IT IS ASKING WHERE THE PLAYER WANTS TO PUT THE TOKEN
        while c1 not in '0123456':  # THIS MAKES SURE THE PLAYER ENTERS NUMBERS 0-6
            print("Columns are numbered 0-6. Choose a number.")  # SO IF THEY DON'T, IT WILL TELL THEM TO DO IT AGAIN
            c1 = input(str(p1)+", your token is X. What column do you want to play in? ")
        c1 = int(c1)    
        for i in board:      # NEXT, THE SEVEN LOOPS BELOW PUT THE TOKEN WHERE THE PLAYER WANTS IT
            if i[0] != 'X' and i[0] != 'O': # MAKES SURE THE SPOT ISN'T TAKEN
                if c1 == 0:         # IF 0 IS THE COLUMN THE PLAYER WANTS TO PUT X IN
                    i[0] = 'X'   # CHANGES THE . TO X
                    break       # BREAK IF THEY PUT AN X IS SO THAT IT ONLY PUTS ONE X...
        for i in board:                       
            if i[1] != 'X' and i[1] != 'O':
                if c1 == 1:
                    i[1] = 'X'
                    break       
        for i in board:
            if i[2] != 'X' and i[2] != 'O':
                if c1 == 2:
                    i[2] = 'X'
                    break            
        for i in board:
            if i[3] != 'X' and i[3] != 'O':
                if c1 == 3:
                    i[3] = 'X'
                    break
        for i in board:
            if i[4] != 'X' and i[4] != 'O':
                if c1 == 4:
                    i[4] = 'X'
                    break
        for i in board:
            if i[5] != 'X' and i[5] != 'O':
                if c1 == 5:
                    i[5] = 'X'
                    break
        for i in board:
            if i[6] != 'X' and i[6] != 'O':
                if c1 == 6:
                    i[6] = 'X'
                    break
        print('')                # THE NEXT FEW LINES PRINT THE BOARD BY EACH ITEM IN THE LIST BOARD, IT STARTS FROM THE LAST ITEM
        print('0 1 2 3 4 5 6')
        print(" ".join(board[5]))
        print(" ".join(board[4]))
        print(" ".join(board[3]))
        print(" ".join(board[2]))
        print(" ".join(board[1]))
        print(" ".join(board[0]))
        print('')
        if check_horizontal_win() is True:    # SO NOW, IF THERE IS A WIN, THE LOOP WILL BREAK AND THE GAME WILL BE OVER AND IT WILL PRINT WHO THE WINNER IS
            print(str(p1)+", you won! Congrats!")
            break  
        if check_vertical_win() is True:  
            print(str(p1)+", you won! Have a good day!")
            break
        if check_diagonal_win() is True:  
            print(str(p1)+", you're the winner! Good job!")
            break
        
        
        c2 = input(str(p2)+", your token is O. What column do you want to play in? ")  # NOW IT IS THE SECOND PLAYER'S TURN
        while c2 not in '0123456':
            print("Columns are numbered 0-6. Choose a number.")
            c2 = input(str(p2)+", your token O. What column do you want to play in? ")
        c2 = int(c2)
        for i in board:
            if i[0] != 'O' and i[0] != 'X':
                if c2 == 0:
                    i[0] = 'O'
                    break
        for i in board:
            if i[1] != 'O' and i[1] != 'X':
                if c2 == 1:
                    i[1] = 'O'
                    break
        for i in board:
            if i[2] != 'O' and i[2] != 'X':
                if c2 == 2:
                    i[2] = 'O'
                    break       
        for i in board:
            if i[3] != 'O' and i[3] != 'X':
                if c2 == 3:
                    i[3] = 'O'
                    break          
        for i in board:
            if i[4] != 'O' and i[4] != 'X':
                if c2 == 4:
                    i[4] = 'O'
                    break
        for i in board:
            if i[5] != 'O' and i[5] != 'X':
                if c2 == 5:
                    i[5] = 'O'
                    break
        for i in board:
            if i[6] != 'O' and i[6] != 'X':
                if c2 == 6:
                    i[6] = 'O'
                    break
        print('')
        print('0 1 2 3 4 5 6')
        print(" ".join(board[5]))
        print(" ".join(board[4]))
        print(" ".join(board[3]))
        print(" ".join(board[2]))
        print(" ".join(board[1]))
        print(" ".join(board[0]))
        print('')
        if check_horizontal_win() is True:
            print(str(p2)+", you win! CONGRATS!")
            break
        if check_vertical_win() is True:
            print(str(p2)+", YOU WON! Have a good day!")
            break
        if check_diagonal_win() is True:
            print(str(p2)+", you're the winner! GREAT job!")
            break

       
            
