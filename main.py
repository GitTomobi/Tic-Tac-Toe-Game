import random

asciiart = """
Welcome To:
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|

 Lets Play!
"""

bdDict = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}

player1 = ''
player2 = ''
p1_symbol_choice = ''
p2_symbol_choice = ''
comp_symbol_choice = ''
isMultiplayer = False
multiplayer_option = ''
multiplayer_values = ['1', '2']
acceptable_values = range(1,9)
within_values = False
acceptable_symbols = ['X','O']
within_symbols = False
isTriple = False
boardFull = False
replay = ''
replay_values = ['Y', 'N']

def gameIntro():
    print(asciiart)

def playerSetUp():
    global player1, player2, isMultiplayer, multiplayer_option
    player1 = ''
    player2 = ''
    isMultiplayer = False

    while player1 == '':
        player1 = input('What\'s your name Player 1? ')

    while multiplayer_option.isdigit() == False or multiplayer_option not in multiplayer_values:
        multiplayer_option = input("Would you like to play single player or multiplayer \'1\' or \'2\'? ")

        if multiplayer_option not in multiplayer_values:
            print('That is not an option')
        else:
            isMultiplayer = True

    if isMultiplayer == True:
        while player2 == '':
            player2 = input('What\'s your name Player 2? ')

def playerSymbolChoice():
    global p1_symbol_choice, p2_symbol_choice, comp_symbol_choice
    
    while p1_symbol_choice not in acceptable_symbols:
        p1_symbol_choice = input(f'Greetings, {player1}! What symbol do you want to use \'X\' or \'O\' ? ')

        if p1_symbol_choice.isdigit() == True:
                print('Do not enter numerical values. Only \'X\' or \'O\'.')
        
        if p1_symbol_choice.isdigit() == False:
            if p1_symbol_choice in acceptable_symbols:
                within_symbols = True
            else:
                pass

    # Symbol Assignment
    if p1_symbol_choice == 'X' and isMultiplayer == False:
        comp_symbol_choice = 'O'
    elif p1_symbol_choice == 'X' and isMultiplayer == True:
        p2_symbol_choice = 'O'
    elif p1_symbol_choice == 'O' and isMultiplayer == True:
        p2_symbol_choice = 'X'
    else:
        comp_symbol_choice = 'X'

def displayTestBoard():
    board = f"""
                        |            |
                        |            |     
                  {bdDict['7']}     |      {bdDict['8']}     |     {bdDict['9']}
                        |            |
             ___________|____________|_____________
                        |            |
                        |            |
                  {bdDict['4']}     |      {bdDict['5']}     |     {bdDict['6']}
                        |            |
             ___________|____________|_____________
                        |            |
                        |            |
                  {bdDict['1']}     |      {bdDict['2']}     |     {bdDict['3']}
                        |            |
                        |            |
"""
    print(board)

def userChoice(choice, symbol):
    bdDict[choice] = symbol
    displayTestBoard()

def compRand():
    return random.randint(1, 9)

def compChoice():
    making_choice = True

    while making_choice is True:
        compRandNum = 0
        compRandNum = compRand()
        if bdDict[str(compRandNum)] == ' ':
            userChoice(str(compRandNum), comp_symbol_choice)
            making_choice = False
        elif ' ' not in bdDict.values():
            making_choice = False
        else:
            print('Computer: This spot is taken already')
            making_choice = True

def winState():
    # Check for triple on player 1s symbol
    if bdDict['1'] == p1_symbol_choice and bdDict['2'] == p1_symbol_choice and bdDict['3'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['4'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['6'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['7'] == p1_symbol_choice and bdDict['8'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['1'] == p1_symbol_choice and bdDict['4'] == p1_symbol_choice and bdDict['7'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['2'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['8'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['3'] == p1_symbol_choice and bdDict['6'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['1'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['3'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['7'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    # Check for triple on computers symbol
    if bdDict['1'] == comp_symbol_choice and bdDict['2'] == comp_symbol_choice and bdDict['3'] == comp_symbol_choice:
        print('Computer wins!!')
        return True

    if bdDict['4'] == comp_symbol_choice and bdDict['5'] == comp_symbol_choice and bdDict['6'] == comp_symbol_choice:
        print('Computer wins!!')
        return True
    
    if bdDict['7'] == comp_symbol_choice and bdDict['8'] == comp_symbol_choice and bdDict['9'] == comp_symbol_choice:
        print('Computer wins!!')
        return True

    if bdDict['1'] == comp_symbol_choice and bdDict['4'] == comp_symbol_choice and bdDict['7'] == comp_symbol_choice:
        print('Computer wins!!')
        return True

    if bdDict['2'] == comp_symbol_choice and bdDict['5'] == comp_symbol_choice and bdDict['8'] == comp_symbol_choice:
        print('Computer wins!!')
        return True
    
    if bdDict['3'] == comp_symbol_choice and bdDict['6'] == comp_symbol_choice and bdDict['9'] == comp_symbol_choice:
        print('Computer wins!!')
        return True
    
    if bdDict['1'] == comp_symbol_choice and bdDict['5'] == comp_symbol_choice and bdDict['9'] == comp_symbol_choice:
        print('Computer wins!!')
        return True
    
    if bdDict['3'] == comp_symbol_choice and bdDict['5'] == comp_symbol_choice and bdDict['7'] == comp_symbol_choice:
        print('Computer wins!!')
        return True

def multiPlayerWinState():
    # Check for triple on player 1s symbol
    if bdDict['1'] == p1_symbol_choice and bdDict['2'] == p1_symbol_choice and bdDict['3'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['4'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['6'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['7'] == p1_symbol_choice and bdDict['8'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['1'] == p1_symbol_choice and bdDict['4'] == p1_symbol_choice and bdDict['7'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    if bdDict['2'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['8'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['3'] == p1_symbol_choice and bdDict['6'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['1'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['9'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True
    
    if bdDict['3'] == p1_symbol_choice and bdDict['5'] == p1_symbol_choice and bdDict['7'] == p1_symbol_choice:
        print(f'{player1} wins!!')
        return True

    # Check for triple on Player 2s symbol
    if bdDict['1'] == p2_symbol_choice and bdDict['2'] == p2_symbol_choice and bdDict['3'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True

    if bdDict['4'] == p2_symbol_choice and bdDict['5'] == p2_symbol_choice and bdDict['6'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True
    
    if bdDict['7'] == p2_symbol_choice and bdDict['8'] == p2_symbol_choice and bdDict['9'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True

    if bdDict['1'] == p2_symbol_choice and bdDict['4'] == p2_symbol_choice and bdDict['7'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True

    if bdDict['2'] == p2_symbol_choice and bdDict['5'] == p2_symbol_choice and bdDict['8'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True
    
    if bdDict['3'] == p2_symbol_choice and bdDict['6'] == p2_symbol_choice and bdDict['9'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True
    
    if bdDict['1'] == p2_symbol_choice and bdDict['5'] == p2_symbol_choice and bdDict['9'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True
    
    if bdDict['3'] == p2_symbol_choice and bdDict['5'] == p2_symbol_choice and bdDict['7'] == p2_symbol_choice:
        print(f'{player2} wins!!')
        return True

def singlePlayerLoop():
    global isTriple

    while isTriple is False:
    #Clear the screen
    #os.system('cls')
    
        print(f'{player1} is: {p1_symbol_choice}')
        print(f'Computer is: {comp_symbol_choice}')
        
        # Display the board
        print('Here is the board: \n')
        displayTestBoard()

        p1_choice = ''    

        #CHECK USER CHOICE
        while p1_choice.isdigit() == False or within_values == False:
            p1_choice = input("Please choose a number position (1-9): ")
            
            if p1_choice.isdigit() == False:
                print('Do not enter letters. Only numerical values (1-9): ')

            if int(p1_choice) in acceptable_values:
                within_values = True
            
            if bdDict[p1_choice] == ' ':
                userChoice(p1_choice, p1_symbol_choice)
            else:
                print('This spot is taken already')
                within_values = False


        #CHECK WIN STATE
        if winState() == True:
            isTriple = True
            break
        elif ' ' not in bdDict.values():
            boardFull = True
            print('Its a Tie!')
            break

        #CHECK COMPUTER CHOICE    
        compChoice()

        #CHECK WIN STATE
        if winState() == True:
            isTriple = True
            break
        elif ' ' not in bdDict.values():
            boardFull = True
            print('Its a Tie!')
            break

def multiPlayerLoop():
    global isTriple
    while isTriple is False:
    #Clear the screen
    #os.system('cls')
    
        print(f'{player1} is: {p1_symbol_choice}')
        print(f'{player2} is: {p2_symbol_choice}')
        
        # Display the board
        print('Here is the board: \n')
        displayTestBoard()

        p1_choice = ''
        p2_choice = ''    

        #CHECK PLAYER 1 CHOICE
        while p1_choice.isdigit() == False or within_values == False:
            p1_choice = input(f" {player1}, please choose a number position (1-9): ")
            
            if p1_choice.isdigit() == False:
                print('Do not enter letters. Only numerical values (1-9): ')

            if int(p1_choice) in acceptable_values:
                within_values = True
            
            if bdDict[p1_choice] == ' ':
                userChoice(p1_choice, p1_symbol_choice)
            else:
                print('This spot is taken already')
                within_values = False


        #CHECK WIN STATE
        if multiPlayerWinState() == True:
            isTriple = True
            break
        elif ' ' not in bdDict.values():
            boardFull = True
            print('Its a Tie!')
            break

        #CHECK PLAYER 2 CHOICE    
        while p2_choice.isdigit() == False or within_values == False:
            p2_choice = input(f"{player2}, please choose a number position (1-9): ")
            
            if p2_choice.isdigit() == False:
                print('Do not enter letters. Only numerical values (1-9): ')

            if int(p2_choice) in acceptable_values:
                within_values = True
            
            if bdDict[p2_choice] == ' ':
                userChoice(p2_choice, p2_symbol_choice)
            else:
                print('This spot is taken already')
                within_values = False
        
        print(bdDict)

        #CHECK WIN STATE
        if multiPlayerWinState() == True:
            isTriple = True
            break
        elif ' ' not in bdDict.values():
            boardFull = True
            print('Its a Tie!')
            break

def TicTacToe():
    #Title Introduction
    gameIntro()

    #Player set up
    playerSetUp()

    #Player symbol choice
    playerSymbolChoice()

    # Main game loop
    if isMultiplayer == True:
        multiPlayerLoop()
    else:
        singlePlayerLoop()
        print('test')
    
    replayGame()

def replayGame():
    global isTriple, player1, player2, isMultiplayer, multiplayer_option, p1_symbol_choice, p2_symbol_choice, comp_symbol_choice, within_values, within_symbols, boardFull, bdDict, replay
    
    while replay not in replay_values:
        replay = input('Would you like to play again \'Y\' \'N\'? ')

        if replay not in replay_values:
            print('That is not an option')
        else:
            pass

    if replay == 'Y':
        isTriple = False
        player1 = ''
        player2 = ''
        isMultiplayer = False
        multiplayer_option = ''
        p1_symbol_choice = ''
        p2_symbol_choice = ''
        comp_symbol_choice = ''
        within_values = False
        within_symbols = False
        boardFull = False
        replay = ''
        bdDict = {
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' '
    }
        TicTacToe()
    elif replay == 'N':
        pass
    else:
        pass
        

################### GAME STARTS HERE ####################

TicTacToe()

print('\nGAME OVER\nThanks for Playing!')