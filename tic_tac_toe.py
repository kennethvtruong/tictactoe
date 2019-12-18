
class TicTacToe:
    def __init__(self, player1, player2, win):
        self.player1 = player1
        self.player2 = player2
        self.win = win
    def turns(self):
        for turn in range(100):
            if turn % 2 == 0:
                self.player1 = input("Where would you like to place the X? ")
                if self.player1 == "1,1":
                    row1[0] = " X "
                elif self.player1 == "2,1":
                    row2[0] = " X "
                elif self.player1 == "3,1":
                    row3[0] = " X "
                elif self.player1 == "1,2":
                    row1[1] = " X "
                elif self.player1 == "1,3":
                    row1[2] = " X "
                elif self.player1 == "2,2":
                    row2[1] = " X "
                elif self.player1 == "2,3":
                    row2[2] = " X "
                elif self.player1 == "3,2":
                    row3[1] = " X "
                elif self.player1 == "3,3":
                    row3[2] = " X "
                else:
                    print("Invalid, try again.")
                print(row1)
                print(row2)
                print(row3)
                my_tic.win_condition()
            else:
                self.player2 = input("Where would you like to place the O? ")
                if self.player2 == "1,1":
                    row1[0] = " O "
                elif self.player2 == "2,1":
                    row2[0] = " O "
                elif self.player2 == "3,1":
                    row3[0] = " O "
                elif self.player2 == "1,2":
                    row1[1] = " O "
                elif self.player2 == "1,3":
                    row1[2] = " O "
                elif self.player2 == "2,2":
                    row2[1] = " O "
                elif self.player2 == "2,3":
                    row2[2] = " O "
                elif self.player2 == "3,2":
                    row3[1] = " O "
                elif self.player2 == "3,3":
                    row3[2] = " O "
                else:
                    print("Invalid, try again.")
                print(row1)
                print(row2)
                print(row3)
                my_tic.win_condition()
    def win_condition(self):
        conditions = [(row1[0] == row1[1] == row1[2]) == 1,
                        (row2[0] == row2[1] == row2[2]) == 1,
                        (row3[0] == row3[1] == row3[2]) == 1,
                        (row3[0] == row3[1] == row3[2]) == 1,
                        (row1[0] == row2[1] == row3[2]) == 1,
                        (row3[0] == row2[1] == row1[2]) == 1,
                        (row1[0] == row2[0] == row3[0]) == 1,
                        (row1[1] == row2[1] == row3[1]) == 1,
                        (row1[2] == row2[2] == row3[2]) == 1]
        for a in conditions:
            if a == 1:
                print("Congrats, you have won.")
                self.win = True
                quit()
            if not self.win:
                print("You have lost.")
row1 = ["1,1", "1,2", "1,3"]
row2 = ["2,1", "2,2", "2,3"]
row3 = ["3,1", "3,2", "3,3"]

my_tic = TicTacToe("X", "O", True)
my_tic.turns()
