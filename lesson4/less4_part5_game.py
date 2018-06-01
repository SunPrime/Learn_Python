class StopGame(Exception):
    pass

class Game:
    def __init__(self, player1, player2, user_interface):
        self.player1 = player1
        self.player2 = player2
        self.user_interface = user_interface

    def start_game(self):
        while True:
            try:
                self.step_player(self.player1)
                self.step_player(self.player2)
            except StopGame:
                break


    def step_player(self, player):
            if not player.is_free_cell():
                self.user_interface.show_draw()
                raise StopGame
            succes = False
            while not succes:
                try:
                    x, y = player.generation_step()
                except NotImplementedError:
                    x, y = self.user_interface.get_coords()
                succes = player.step(x, y)
            self.user_interface.show_field(player.show_field())
            if player.is_winner():
                self.user_interface.show_winner(player.name)
                raise StopGame

class User_interface:
    def show_draw(self):
        print('draw')

    def get_coords(self):
        return map(int, input('Ведите число: ').split(' '))

    def show_field(self, field):
        for line in field:
            print(line)

    def show_winner(self, winner):
        print(winner + ' is winner')

class Player:
    def __init__(self, field, mark, name):
        self.field = field
        self.mark = mark
        self.name = name

    def is_free_cell(self):
        return self.field.is_free_cell()

    def generation_step(self):
        raise NotImplementedError

    def step(self, x, y):
        if not (0 <= x < 3 and 0 <= y < 3 and self.field.check_cell(x, y)):
            return False
        self.field.change_state(x, y)
        return True

    def is_winner(self):
        return self.field.is_line(self.mark)

    def show_field(self):
        return self.field.show()

class Computer(Player):
    def __init__(self, field, mark, name):
        Player.__init__(self, field, mark, name)

    def generation_step(self):
        return self.field.get_free_cell()

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
            return False

    def change_status(self, x, y, mark):
        if self.check_cell(x, y):
            self.field[x][y].status = mark

    def show(self):
        field = []
        for i in range(3):
            line = ''
            for j in range(3):
                line += self.field[i][j].status + '|'
            field.append(line)
        return field

    def get_free_cell(self):
        for i in range(3):
            for j in range(3):
                if self.field[i][j].status == '_':
                    return i, j


class Cell:
    def __init__(self, status):
        self.status = status


fieldA = Field()
person1 = Player(fieldA, 'X', 'Human')
person2 = Computer(fieldA, 'O', 'Computer')
interface = User_interface()
game1 = Game(person1, person2, interface)
game1.start_game()