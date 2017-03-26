from random import randint

class Battleship:
    global board  #Create an empty array to represent game board
    board = []

    def new_board(self, board):           #Creates a new 5 x 5 board with "O"'s for each position on the board
        turn = 0
        for x in range(5):
            board.append(["O"] * 5)
        return board

    def print_board(self, board):         #Custom print to organize game board
        for row in board:
            print " ".join(row)

    def random_row(self, board):  #picks a random row for the battleship
        return randint(0, len(board) - 1)

    def random_col(self, board):          #picks a random col for the battleship
        return randint(0, len(board[0]) - 1)
    

    def new_game(self, board):            #Creates a new board, resets guess attempts
        self.board = []
        self.new_board(board)

        ship_row = self.random_row(board)
        ship_col = self.random_col(board)


        print "Let's play Battleship!"
        self.print_board(board)

        for turn in range(4):       
            guess_row = input("Guess Row:")
            guess_col = input("Guess Col:")

            if guess_row == ship_row and guess_col == ship_col:
                print "Congratulations! You sunk my battleship!"
                break
            else:
                if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print "Oops, that's not even in the ocean."
                elif (board[guess_row][guess_col] == "X"):
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    board[guess_row][guess_col] = "X"
            print (turn+1)          #Display how many turns have been used
            self.print_board(board)

        if (turn + 1) == 4:
            print "Game Over"

    def play_again(self):
        userInput = raw_input("Would you like to play again? Enter y/n :")
        if userInput == 'n':
            raw_input("Press Enter to exit")
        elif userInput == 'y':
            self.new_game(self.board)
        else:
            print "Invalid selection"
            self.playAgain()


def main():

    x = Battleship()

    x.new_game(board)

    x.play_again()

if __name__ == "__main__":
    main()
