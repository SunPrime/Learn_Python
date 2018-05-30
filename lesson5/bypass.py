def show(field):
    for i in range(10):
        line = ''
        for j in range(10):
            line += field[i][j] + '|'
        field.append(line)
        print(line)
    print()

def bypass(field, i, j):
    if (field[i][j-1] == '_' or field[i][j-1] == '+'):
        field[i][j-1] = '+'
    if field[i][j-1] == 'X':
        bypass(field, i, j-1)

    if (field[i-1][j-1] == '_' or field[i-1][j-1] == '+'):
        field[i-1][j-1] = '+'
    if field[i-1][j-1] == 'X':
        bypass(field, i-1, j-1)

    if (field[i-1][j] == '_' or field[i-1][j] == '+'):
        field[i-1][j] = '+'
    if field[i-1][j] == 'X':
        bypass(field, i-1, j)

    if (field[i-1][j+1] == '_' or field[i-1][j+1] == '+'):
        field[i-1][j+1] = '+'
    if field[i-1][j+1] == 'X':
        bypass(field, i-1, j+1)

    if (field[i][j+1] == '_' or field[i][j+1] == '+'):
        field[i][j+1] = '+'
    if field[i][j+1] == 'X':
        bypass(field, i, j+1)

    if (field[i+1][j+1] == '_' or field[i+1][j+1] == '+'):
        field[i+1][j+1] = '+'
    if field[i+1][j+1] == 'X':
        bypass(field, i+1, j+1)

    if (field[i+1][j] == '_' or field[i+1][j] == '+'):
        field[i+1][j] = '+'
    if field[i+1][j] == 'X':
        bypass(field, i+1, j)

    if (field[i+1][j-1] == '_' or field[i+1][j-1] == '+'):
        field[i+1][j-1] = '+'
    if field[i+1][j-1]:
        bypass(field, i+1, j-1)


field = [['_' for j in range(10)] for i in range(10)]
show(field)
field[5][3] = 'X'
field[4][3] = 'X'
field[6][3] = 'X'
show(field)
bypass(field, 6, 3)
show(field)