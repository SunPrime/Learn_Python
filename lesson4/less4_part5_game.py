class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        while True:
            if not self.player1.is_free_cell():
                return 'draw'
            self.player1.step()
            if self.player1.is_winner():
                return 'player1 is winner'
            if not self.player2.is_free_cell():
                return 'draw'
            self.player2.step()
            if self.player2.is_winner():
                return 'player1 is winner'

class Player:
    def __init__(self, field, mark):
        self.field = field
        self.mark = mark

    def is_free_cell(self):
        return self.field.is_free_cell()

    def step(self):
        pass

    def is_winner(self):
        return self.field.is_line(self.mark)

class Human(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        x = int(input())
        y = int(input())
        self.field.change_status(x, y, self.mark)
        self.field.show()

class Computer(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        x, y = self.field.get_free_cell()
        self.field.change_status(x, y, self.mark)
        self.field.show()

class Cell:
    def __init__(self):
        self.status = 'p'
