import numpy
import random
import copy

class ConnectFour:
    def __init__(self):
        self._wide = 7
        self._high = 6
        self.board = numpy.zeros(shape=(self._high, self._wide), dtype=int)

    def print_bord(self):
        for i in self.board[::-1]:
            print(i)

    def insert_disc(self, index):
        for i in range(self._high):
            if not self.board[i, index]:
                self.board[i, index] = self.player
                return
        raise IndexError(f"There is no space in the board in index {index}")

    def get_board_cell(self, row, col):
        if self.board[row, col]:
            return self.board[row, col]
        return "insert disc into " + str((row, col))

    def is_place(self, index):
        return not self.board[self._high - 1][index]



    def play_as_computer(self):
        print("computer is playing")
        res = self.calculate_best_shape()
        self.insert_disc(res)

    def player_play(self):
        while True:
            try:
                col = int(input(f'player {self.player}: insert disc'))
                self.insert_disc(col)
                break
            except IndexError as e:
                print(e)



    def is_equal(self, arr, value):
        if len(arr) < 4:
            return False
        for i in arr:
            if i != value:
                return False
        return True
    def is_win(self):
        for i in self.board:
            if (self.is_equal(i[:4], self.player) or self.is_equal(i[1:5], self.player) or self.is_equal(i[2:6], self.player) or self.is_equal(i[3:], self.player)):
                return True

        for i in range(self._wide):
            if self.is_equal(self.board[:,i][:4], self.player) or self.is_equal(self.board[:,i][1:], self.player):
                return True

        diags = [self.board[::-1, :].diagonal(i) for i in range(-2, 3)]
        diags.extend(self.board.diagonal(i) for i in range(3, -2, -1))
        for i in diags:
            if self.is_equal(i[:4], self.player) or self.is_equal(i[1:5], self.player) or self.is_equal(i[2:], self.player):
                return True

        return False


    def set_next_player(self):
        self.player = 1 if self.player is 2 else 2

    def calculate_best_shape(self):
        for i in range(self._wide):
            temp = ConnectFour()
            temp.board = copy.deepcopy(self.board)
            temp.player = self.player
            temp.insert_disc(i)
            if temp.is_win():
                return i
        while True:
            insert = random.randint(0, self._wide - 1)
            if self.is_place(insert):
                return insert










    def play(self):
        answer = input("Do you want to play against the computer (y/n)?")
        self.computer = (answer == 'y')
        self.player = 2
        if not self.computer:
            print("# start a game of 2 players")
        self.print_bord()
        while not self.is_game_over():
            self.set_next_player()
            self.play_as_computer() if self.computer and self.player == 2 else self.player_play()
            self.print_bord()
            if self.is_win():
                print("The computer won!!") if self.computer and self.player == 2 else print(f'player {self.player} won!!')
                exit(0)




    def is_game_over(self):
        for i in range(self._wide):
                if not self.board[self._high - 1][i]:
                    return False
        return True




if __name__ == "__main__":
    game = ConnectFour()
    game.play()

