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
                return 'player2 is winner'

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
        while True:
            try:
                x = int(input("Введите х: "))
                if 0 <= x < 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Введите 0, 1 или 2")
        while True:
            try:
                y = int(input("Введите y: "))
                if 0 <= y < 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Введите 0, 1 или 2")
        self.field.change_status(x, y, self.mark)
        self.field.show()

class Computer(Player):
    def __init__(self, field, mark):
        Player.__init__(self, field, mark)

    def step(self):
        x, y = self.field.get_free_cell()
        self.field.change_status(x, y, self.mark)
        self.field.show()

class Field:
    def __init__(self):
        self.field = []
        self.set_field()

    def set_field(self):
        cell = Cell()
        self.field = [[cell.status for j in range(3)] for i in range(3)]

    def is_free_cell(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 'p':
                    return True

    def is_line(self, mark):
        for i in range(3):
            for j in range(3):
                if (self.field[i][0] == mark and self.field[i][1] == mark and self.field[i][2] == mark):
                    return True
                if (self.field[0][j] == mark and self.field[1][j] == mark and self.field[2][j] == mark):
                     return True
            if (self.field[0][0] == mark and self.field[1][1] == mark and self.field[2][2] == mark):
                return True
            if (self.field[0][2] == mark and self.field[1][1] == mark and self.field[2][0] == mark):
                return True

    def change_status(self, x, y, mark):
        self.field[x][y] = mark

    def show(self):
        for i in range(3):
            print(self.field[i])
        print()

    def get_free_cell(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == 'p':
                    return i, j


class Cell:
    def __init__(self):
        self.status = 'p'


fieldA = Field()
person1 = Human(fieldA, 'X')
person2 = Computer(fieldA, 'O')
game1 = Game(person1, person2)
game1.start_game()