'''
Language: Python
--------------------
Main file. It has the two mode; one-move mode and interactive mode. It calls the functions in the other py file MaxConnect4Game.py
'''
import sys  #importing all system file
from MaxConnect4Game import MaxConnect4game     #used for creating object of other file    

def humanPlay(gameboard):       # human function taking the input and putting the element in it
    while gameboard.getPieceCount() != 42:  # checking if the board is empty or not
        print(" Human's turn") 
        print(" ------- ----")
        userMove = int(input("Enter a column number (1-7): "))  # taking input which column number should be enter
        if not 0 < userMove < 8:    # checking if it is valid input or not
            print("Column invalid! Enter Again.")
            continue
        if not gameboard.playPiece(userMove - 1):
            print("Column number: %d is full. Try other column." % userMove)
            continue
        print("Your made move: " + str(userMove))
        gameboard.displayGB()   # displaying the game board
        gameboard.gameFile = open("human.txt", 'w')  # displaying it in the txt file
        gameboard.printGameBoardToFile()
        gameboard.gameFile.close()  # file closing
        if gameboard.getPieceCount() == 42:     # checking if the borad is full
            print("No more moves possible, Game Over!")
            gameboard.scoreCount()  # printing the score
            print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
            break
        else:   # computer move
            print("Computer is conputing based on next " + str(gameboard.depth) + " steps...")
            gameboard.changeMove()  # changing the player to other player
            gameboard.aiPlay()  # computing the computer move with the minmax alpha beta puring
            gameboard.displayGB()   # displaying game borad
            gameboard.gameFile = open('computer.txt', 'w')  # printing output to file
            gameboard.printGameBoardToFile()
            gameboard.gameFile.close()  # file closing
            gameboard.scoreCount()  # printing score count
            print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))

def interactiveMode(gameboard, nextPlayer):     # interactive mode
    print('Current Board state')
    gameboard.displayGB()   # displaying game board
    gameboard.scoreCount()  # displaying score
    print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
    if nextPlayer == 'human-next':  # checking who is the next player from argv
        humanPlay(gameboard)    # human function 
    else:
        gameboard.aiPlay()  # computign the computer move
        gameboard.gameFile = open('computer.txt', 'w')  # printing the result into the file
        gameboard.printGameBoardToFile()
        gameboard.gameFile.close()  # closing the file
        gameboard.displayGB()   # dislaying the game board
        gameboard.scoreCount()  # displaying the score 
        print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
        humanPlay(gameboard)    # human turn next

    if gameboard.getPieceCount() == 42: # displaying the final result after all the piece in the borad is full
        if gameboard.player1Score > gameboard.player2Score:
            print("Player 1 wins")
        if gameboard.player1Score == gameboard.player2Score:
            print("The game is a Tie")
        if gameboard.player1Score < gameboard.player2Score:
            print("Player 2 wins")
        print("Game Over")


def oneMoveMode(gameboard):     # one move mode
    if gameboard.pieceCount >= 42:  # checking if all the piece are filled, then exit
        print('Game board is full !\n Game Over...')
        sys.exit(0)
    print ('Gameboard state before move:')
    gameboard.displayGB()   # displaying game board
    gameboard.aiPlay()      # Computing the computer move
    print ('Gameboard state after move:')
    gameboard.displayGB()   # displaying game board
    gameboard.scoreCount()  # displaying score
    print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
    gameboard.printGameBoardToFile()    # printing the game board into file
    gameboard.gameFile.close()      # close file

def main(argv): 
    gameboard = MaxConnect4game()   #object of other file
    try:
        gameboard.gameFile = open(argv[2], 'r')     #reading the input file
        fileLines = gameboard.gameFile.readlines()
        gameboard.gameboard = [[int(char) for char in line[0:7]] for line in fileLines[0:-1]]
        gameboard.currentMove = int(fileLines[-1][0])
        gameboard.gameFile.close()
    except:
        print('File not found, begin new game.')
        gameboard.currentMove = 1
    gameboard.checkPieceCount()     # checking all the elements added is true or not
    gameboard.depth = argv[4]   # depth taken from argv
    if argv[1] == 'one-move':   #for one move mode
        try:
            gameboard.gameFile = open(argv[3], 'w')
        except:
            sys.exit('Error while opening output file.')
        oneMoveMode(gameboard)
    else:   # for interactive mode
        interactiveMode(gameboard, argv[3])

main(sys.argv)
# main function
