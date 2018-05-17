class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_game(self):
        while True:
            self.player1.step()
            if self.player1.is_winner():
                print('player1 is winner')
                return
            self.player2.step()
            if self.player2.is_winner():
                print('player2 is winner')
                return

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
                x, y = map(int, input("Введите х, y: ").split(','))
                if 0 <= x < 3:
                    if 0 <= y < 3:
                        if self.field.check_cell(x, y):
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
        self.field = [[Cell('_') for j in range(3)] for i in range(3)]

    def is_free_cell(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j].status == '_':
                    return True

    def is_line(self, mark):
        for i in range(3):
            for j in range(3):
                if (self.field[i][0].status == mark and self.field[i][1].status == mark and self.field[i][2].status == mark):
                    return True
                if (self.field[0][j].status == mark and self.field[1][j].status == mark and self.field[2][j].status == mark):
                     return True
        if (self.field[0][0].status == mark and self.field[1][1].status == mark and self.field[2][2].status == mark):
            return True
        if (self.field[0][2].status == mark and self.field[1][1].status == mark and self.field[2][0].status == mark):
            return True

    def check_cell(self, x, y):
        if self.field[x][y].status == '_':
            return True
        else:
            print('Выберите другую клетку')
            return False

    def change_status(self, x, y, mark):
        if self.check_cell(x, y):
            self.field[x][y].status = mark

    def show(self):
        for i in range(3):
            line = ''
            for j in range(3):
                line += self.field[i][j].status + '|'
            print(line)
        print()

    def get_free_cell(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j].status == '_':
                    return i, j


class Cell:
    def __init__(self, status):
        self.status = status


fieldA = Field()
person1 = Human(fieldA, 'X')
person2 = Computer(fieldA, 'O')
game1 = Game(person1, person2)
game1.start_game()
