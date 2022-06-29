''' This application is a SUDOKU Puzzle Game that loads and saves the current status of the game board into a '<code>.txt' file.
AUTHOR  : Rodriguez, Clarissa Gallo
DATE    : 17 DEC 2020 '''

import os
import pyfiglet

# Shows main menu
def show_menu():
    title = pyfiglet.figlet_format("SUDO-kun QUEST")
    print('\n' + title)
    print("You are about to enter the headquarters of your arch nemesis.\n" + "At the front of its cryptic door, you see a weathered old sergeant covered with blood." + "\nAs you near, he frighteningly warned you..." + "\n'Do not dare to enter that place." + "\nYour co-agents eat each other brains.'" + "\n\nThen your best friend begged as he's trying not to come out of breath..." + "\n'SUDO-KUN!!! SU--DO HELP!! HELP!'")
    print('\na. CONTINUE')
    print("b. Nah. I went here just to solve a 9x9 PUZZLE")
    print("c. Hmmm but lemme try a 16x16 PUZZLE coz I think I'm smart")
    print("x. I'M SCARED... *runs into void*")
    choice = input('\nEnter choice: ')
    return choice

# Loads pre-set boards from files
def loadFromFile(filename):
    board = []
    file = open(filename,'rt') # filename can either be 9x9.txt or 16x16.txt
    lines = file.readlines()
    for line in lines:
        lst = []
        for num in line.split(","):
            lst.append(int(num))
        board.append(lst)
    file.close()
    return board    # 2D list of pre-set board

# Prints the display board
def print_board(puzzle):
    if c == 'b': # 9x9
        top_label = "   1  2  3    4  5  6    7  8  9"
        top_bot = "╟════════════════════════════════╢"
        middle = "╟══════════╬══════════╬══════════╢"
        print(top_label)
        print(top_bot)
        for x in range(9):
            for y in range(9):
                if ((x == 3 or x == 6) and y == 0):
                    print(middle)
                if (y == 0 or y == 3 or y== 6):
                    print("║", end=" ")
                print(" " + str(puzzle[x][y]), end=" ")
                if (y == 8):
                    print("║")
        print(top_bot)

    else: # 16x16
        top_label = "   1   2   3   4    5   6   7   8    9   10  11  12   13  14  15  16"
        top_bot = "╟════════════════════════════════════════════════════════════════════╢"
        middle = "╟════════════════════════════════════════════════════════════════════╢"
        print(top_label)
        print(top_bot)
        for x in range(16):
            for y in range(16):
                if ((x == 4 or x == 8 or x == 12) and y == 0):
                    print(middle)
                if (y == 0):
                    print("║", end=" ")
                if (y == 4 or y == 8 or y == 12):
                    print("║",end="")
                if len(str(puzzle[x][y])) == 1:
                    print(" " + str(puzzle[x][y]), end="  ")
                else:
                    print(" " + str(puzzle[x][y]), end=" ")
                if (y == 15):
                    print("║")
        print(top_bot)

# Finding empty spaces
def find_empty(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 0:
                return (row, col) 
    return None   # if spaces are filled

# Validates the values on row, col, and 3x3 or 4x4 cube
def valid(puzzle, num, pos):    # pos = position
    # Checks row
    for row in range(len(puzzle[0])):
        if puzzle[pos[0]][row] == num and pos[1] != row:    # checks element in each row
            return False

    # Checks column
    for col in range(len(puzzle)):
        if puzzle[col][pos[1]] == num and pos[0] != col:    # checks element in each column   
            return False

    if c == 'b': # 9x9
    # Checks box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if puzzle[i][j] == num and (i,j) != pos:
                    return False
    else:   # 16x16
        box_x = pos[1] // 4
        box_y = pos[0] // 4

        for i in range(box_y*4, box_y*4 + 4):
            for j in range(box_x * 4, box_x*4 + 4):
                if puzzle[i][j] == num and (i,j) != pos:
                    return False

    return True

# Solves sudoku puzzle using backtracking
def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True # SOLVED
    else:
        r, cl = find

    if c == 'b':
        e = 10
    else:
        e = 17

    for row in range(1,e):
        if valid(puzzle, row, (r, cl)):
            puzzle[r][cl] = row

            if solve(puzzle):
                return True
            puzzle[r][cl] = 0 

    return False

# Converts the puzzle into lists within list
def to_list(filename):
    board = []
    for row in range(len(filename)):  
        line = []
        for col in range(len(filename)):  
            line.append(int(filename[row][col]))
        board.append(line)
    return board

# Saves board to file: <code>.txt
def saveToFile(puzzle):
    new_file = open(username,'w+')
    for row in puzzle:
        x = ",".join(map(str,row))
        new_file.write(x + '\n')
    new_file.close()
    return True   

# Asks for the input of the player on the array and his turn
def player_input():
    global y, x, turn
    y = int(input('Enter row no.: '))   # Puzzle's row
    x = int(input('Enter col no.: '))   # Puzzle's column
    y -= 1
    x -= 1
    if lst_puzzle[y][x] == 0:
        turn = int(input('Enter guess: '))  # Player's turned value
        return y, x, turn
    else:
        print("Don't change the puzzle, Sudo-kun. The default value is",lst_puzzle[y][x])
        player_input()

# Updates the board of the player with his turned values if correct
def update(lst_puzzle):
    is_saved =  saveToFile(lst_puzzle)
    if is_saved == True:
        print()
        print_board(lst_puzzle)

# Returns the updated board of the player
def new_board(lst_puzzle):
    clear = lambda:os.system('cls')
    clear()
    print_board(lst_puzzle)
    lst_puzzle[y][x] = turn     # replaces from 0 to turn
    if turn != lst_solved[y][x]:
        print('Wrong. Try again for your best friend, okay?')
        lst_puzzle[y][x] = 0    # brings back the target space into 0
        print_board(lst_puzzle)
        check_turn()
    else:
        print('You got it, Sudo-kun! Diminish all zeroes!.')
        update(lst_puzzle)  # updates the current state of the game
        check_turn()  

# Compares the turned values of the player with the solved puzzle values
def check_turn():
   # Calls the solved puzzle board
    solve(board)
    global lst_solved
    lst_solved = to_list(board) # 2D list of solved puzzle

    # Compares 2D lists of pre-set board and the solved board
    if lst_puzzle == lst_solved: #SOLVED
        confirm = input('\nCONGRATULATIONS, Agent Sudo-kun!' + '\nYou may now enter the door.' + '\nBut maybe -- do you want to take the brain scan again? (y/n)')
        if confirm == 'y':
            clear()
            print('\nReturning to menu ...')
        else:
            clear()
            print("OH YOU'RE IN A RUSH." + "\nReturning to menu ... ")
            show_menu() 
    # If not yet solved    
    else:
        # Player's turn
        player_input()
        new_board(lst_puzzle)

while True:
    c = show_menu()
    clear = lambda:os.system('cls')
    if c =='a' or  c =='A' :
        clear()
        print('''You're trying to open the door but it's TOTALLY LOCKED.
        The door displays what you should do FIRST ...''')
        brainScan = pyfiglet.figlet_format("BRAIN SCAN")
        print(brainScan)
        print('''HOW? HERE ARE THE STEPS:
        ▶ PLAY: 9x9 or 16X16 sudoku puzzle 
        ▶ INPUT: Enter row, column and guess at a time 
        ▶ SEE: Witness your brain capacity, there's an answer checking every TURN
        ▶ FINISH THE QUEST''')
        heads_up = input('\nARE YOU WILLING TO TAKE THE CHALLENGE? (y/n) ')
        if heads_up == 'y':
            clear()
            print('\n Returning to menu ...')
        else:
            clear()
            print("A COWARD INPUT. But because the programmer is good ..." + "\n\nReturning to menu ... ")
    elif c == 'b' or c =='B':
        clear()
        username = input("What's your code, agent? ")
        source = '9x9.txt'
        print('\nSOLVE 9X9 PUZZLE!')
        board = loadFromFile(source)
        print_board(board)
        lst_puzzle = to_list(board)
        check_turn()
    elif c == 'c' or c =='C':
        clear()
        username = input("What's your code, agent? ")
        source = '16x16.txt' 
        print('\nSOLVE 16x16 PUZZLE!')
        board = loadFromFile(source)
        print_board(board)
        lst_puzzle = to_list(board)
        check_turn()
    elif c == 'x' or c =='X':
        clear()
        print("Come back when you're brave enough. Sayōnara!")
        break
    else:
        clear()
        print("Hey, Agent Sudo-kun. Please input the right choice.")