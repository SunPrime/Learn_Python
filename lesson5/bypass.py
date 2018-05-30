def show(field):
    for i in range(10):
        line = ''
        for j in range(10):
            line += field[i][j] + '|'
        field.append(line)
        print(line)
    print()

def cell_mark(i, j):
    if (field[i][j] == '_'):
        field[i][j] = '+'
    if field[i][j] == 'X':
        field[i][j] = 'K'
        bypass(field, i, j)

def bypass(field, i, j):
    field[i][j] = 'K'
    if 0 <= (j - 1):
        cell_mark(i, j - 1)

    if 0 <= (i - 1) and 0 <= (j - 1):
        cell_mark(i - 1, j - 1)

    if 0 <= (i - 1):
        cell_mark(i - 1, j)

    if 0 <= (i - 1) and (j + 1) <= 9:
        cell_mark(i - 1, j + 1)

    if (j + 1) <= 9:
        cell_mark(i, j + 1)

    if (i + 1) <= 9 and (j + 1) <= 9:
        cell_mark(i + 1, j + 1)

    if (i + 1) <= 9:
        cell_mark(i + 1, j)

    if (i + 1) <= 9 and 0 <= (j - 1):
        cell_mark(i + 1, j - 1)


field = [['_' for j in range(10)] for i in range(10)]
field[5][3] = 'X'
field[4][3] = 'X'
field[6][3] = 'X'
field[1][1] = 'X'
field[1][2] = 'X'
field[4][9] = 'X'
field[5][9] = 'X'
field[6][9] = 'X'
field[9][6] = 'X'
field[9][7] = 'X'
field[9][8] = 'X'
field[9][9] = 'X'
show(field)
bypass(field, 6, 3)
bypass(field, 1, 1)
bypass(field, 5, 9)
bypass(field, 9, 9)
show(field)