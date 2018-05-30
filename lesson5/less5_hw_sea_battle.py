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
                self.step_player(self.player1, self.player2)
                self.step_player(self.player2, self.player1)
            except StopGame:
                break

    def step_player(self, player, enemy):
        if not player.is_free_cell():
            self.user_interface.show_draw()
            raise StopGame
        success = False
        while not success:
            try:
                x, y = player.generation_step()
            except NotImplementedError:
                x, y = self.user_interface.get_coords()
            success, state = player.step(enemy.field_of_player, x, y)
            if state:
                self.user_interface.show_state(state)
        self.user_interface.show_field(player.show_field())
        if enemy.is_winner():
            self.user_interface.show_field(enemy.show_field())
            self.user_interface.show_winner(player.name)
            raise StopGame


class User_interface:
    def show_draw(self):
        print('draw')

    def get_coords(self):
        return map(int, input('Input coordinates: ').split(' '))

    def show_field(self, fields):
        for i in range(10):
            print(fields[0][i] + '     ' + fields[1][i])
        print()

    def show_state(self, state):
        print(state)

    def show_winner(self, winner):
        print(winner + ' is winner')

class Player:
    def __init__(self, name):
        self.field_of_player = Field()
        self.set_ships()
        self.field_of_enemy = Field()
        self.name = name

    def set_ships(self):
        self.field_of_player.set_ships4player()

    def is_free_cell(self):
        return self.field_of_enemy.is_free_cell()

    def generation_step(self):
        raise NotImplementedError

    def step(self, field_enemy, x, y):
        if not (0 <= x < 10 and 0 <= y < 10 and field_enemy.check_cell(x, y)):
            return False, False
        status, alive = field_enemy.change_state(x, y)
        self.field_of_enemy.field[x][y].status = status
        if alive == 'Sunk':
            self.field_of_enemy.bypass(x, y)
        return True, alive

    def is_winner(self):
        return self.field_of_player.are_ships_alive()

    def show_field(self):
        return self.field_of_player.show(), self.field_of_enemy.show()

class Computer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def set_ships(self):
        self.field_of_player.set_ships4computer()

    def generation_step(self,):
        return self.field_of_enemy.get_free_cell()


class Field:
    def __init__(self):
        self.field = []
        self.set_field()
        self.ships = []

    def set_field(self):
        self.field = [[Cell('_') for j in range(10)] for i in range(10)]

    def is_free_cell(self):
        for i in range(10):
            for j in range(10):
                cell = self.field[i][j].status
                if (cell == '_' or cell == 'O'):
                    return True

    def check_cell(self, x, y):
        cell = self.field[x][y].status
        if (cell == '_'or cell == 'O'):
            return True
        else:
            return False

    def change_state(self, x, y):
        alive = 'Pass'
        if self.check_cell(x, y):
            status = '+'
            cell = self.field[x][y]
            if cell.status == 'O':
                status = 'X'
                cell.ship.hit()
                alive = cell.ship.is_alive()
                if alive:
                    alive = 'Injured'
                else:
                    alive = 'Sunk'
            cell.status = status
            return status, alive

    def bypass(self, i, j):
        self.field[i][j].status = '#'
        if 0 <= (j - 1):
            self.cell_label(i, j - 1)

        if 0 <= (i - 1) and 0 <= (j - 1):
            self.cell_label(i - 1, j - 1)

        if 0 <= (i - 1):
            self.cell_label(i - 1, j)

        if 0 <= (i - 1) and (j + 1) <= 9:
            self.cell_label(i - 1, j + 1)

        if (j + 1) <= 9:
            self.cell_label(i, j + 1)

        if (i + 1) <= 9 and (j + 1) <= 9:
            self.cell_label(i + 1, j + 1)

        if (i + 1) <= 9:
            self.cell_label(i + 1, j)

        if (i + 1) <= 9 and 0 <= (j - 1):
            self.cell_label(i + 1, j - 1)

    def cell_label(self, i, j):
        cell = self.field[i][j]
        if cell.status == '_':
            cell.status = '+'
        elif cell.status == 'X':
            cell.status = '#'
            self.bypass(i, j)

    def show(self):
        field = []
        for i in range(10):
            line = ''
            for j in range(10):
                line += self.field[i][j].status + '|'
            field.append(line)
        return field

    def get_free_cell(self):
        for i in range(10):
            for j in range(10):
                cell = self.field[i][j].status
                if (cell == '_' or cell == 'O'):
                    return i, j

    def set_ships4player(self):
        self.set_ship_by_coords([[0, 0], [0, 1]])
        self.set_ship_by_coords([[1, 3], [1, 4]])
        self.set_ship_by_coords([[3, 2], [4, 2]])

    def set_ships4computer(self):
        self.set_ship_by_coords([[0, 0], [0, 1], [0, 2]])
        self.set_ship_by_coords([[1, 6], [1, 7]])
        self.set_ship_by_coords([[2, 1], [2, 2], [2, 3], [2, 4]])
        self.set_ship_by_coords([[5, 5], [5, 6], [5, 7]])
        self.set_ship_by_coords([[7, 7]])

    def set_ship_by_coords(self, coords):
        ship = Ship(len(coords))
        for coord in coords:
            cell = self.field[coord[0]][coord[1]]
            cell.status = 'O'
            cell.set_ship(ship)
        self.ships.append(ship)

    def are_ships_alive(self):
        res = 0
        for ship in self.ships:
            if ship.is_alive():
                res += 1
        if res == 0:
            return True


class Ship:
    def __init__(self, alive):
        self.alive = alive

    def hit(self):
        self.alive -= 1

    def is_alive(self):
        return self.alive > 0


class Cell:
    ship = None
    def __init__(self, status):
        self.status = status

    def set_ship(self, ship):
        self.ship = ship


person1 = Player('Human')
person2 = Computer('Computer')
interface = User_interface()
game1 = Game(person1, person2, interface)
interface.show_field(person1.show_field())
interface.show_field(person2.show_field())
game1.start_game()