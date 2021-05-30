import os


# define board
class board:
    # self.player is an object to use in check if there is a winner
    player: object

    def __init__(self):
        self.cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    # display board
    def board_display(self):
        print(" %s|%s|%s" % (self.cells[1], self.cells[2], self.cells[3]))
        print("-------")
        print(" %s|%s|%s" % (self.cells[4], self.cells[5], self.cells[6]))
        print("-------")
        print(" %s|%s|%s" % (self.cells[7], self.cells[8], self.cells[9]))

    # board updater
    def board_updater(self, no_cell, player):
        self.player = player
        if self.cells[no_cell] == " ":
            self.cells[no_cell] = player
        elif self.cells[no_cell] != " ":
            print("\nPlease select a spot that is not taken!")
            no_cell = int(input("\n %s) turn which position you want 1 - 9 : " % player))
            display.board_updater(no_cell, player)

    # clean the cells to play again
    def clean_cells(self):
        self.cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    # check if there is a winner
    def check_if_winner(self):
        if self.cells[1] == self.cells[2] == self.cells[3] == "X" or \
                self.cells[1] == self.cells[2] == self.cells[3] == "O":
            print("The %s wins" % self.player)
            display.game_again()

        elif self.cells[4] == self.cells[5] == self.cells[6] == "X" or \
                self.cells[4] == self.cells[5] == self.cells[6] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[7] == self.cells[8] == self.cells[9] == "X" or \
                self.cells[7] == self.cells[8] == self.cells[9] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[1] == self.cells[5] == self.cells[9] == "X" or \
                self.cells[1] == self.cells[5] == self.cells[9] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[3] == self.cells[5] == self.cells[7] == "X" or \
                self.cells[3] == self.cells[5] == self.cells[7] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[1] == self.cells[4] == self.cells[7] == "X" or \
                self.cells[1] == self.cells[4] == self.cells[7] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[3] == self.cells[6] == self.cells[9] == "X" or \
                self.cells[3] == self.cells[6] == self.cells[9] == "O":
            print("The %s wins" % self.player)
            display.game_again()
        elif self.cells[2] == self.cells[5] == self.cells[8] == "X" or \
                self.cells[2] == self.cells[5] == self.cells[8] == "O":
            print("The %s wins" % self.player)
            display.game_again()

    # Title
    @staticmethod
    def title_header():
        print("Tick Tack Toe")

    # refresh the screen
    @staticmethod
    def screen_refresher():
        # screen cleaner
        os.system("cls")
        # title of the game
        display.title_header()
        # board of the game
        display.board_display()

    # Run the game again or quit
    @staticmethod
    def game_again():
        choice = input("\n -Do you want to play again, (Y/N) ? ")
        if choice.lower() == "y":
            display.clean_cells()
            display.run_program()
        elif choice.lower() == "n":
            quit()

    # running the program
    @staticmethod
    def run_program():
        while True:
            display.screen_refresher()
            player = "X"
            no_cell = int(input("\n X) turn which position you want 1 - 9 : "))
            display.board_updater(no_cell, player)
            display.screen_refresher()
            display.check_if_winner()
            player = "O"
            no_cell = int(input("\n O) turn which position you want 1 - 9 : "))
            display.board_updater(no_cell, player)
            display.screen_refresher()
            display.check_if_winner()

# Universal object
display = board()

