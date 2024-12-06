import sys
sys.setrecursionlimit(10000)


def search_guard(matrix, a, b):
    for i in range(a):
        for j in range(b):
            if matrix[i][j] == '^':
                return [i, j]
    return [-1, -1]


def count_step(bool_matrix, num_row, num_column):
    count = 0
    for r in range(num_row):
        for c in range(num_column):
            if bool_matrix[r][c] == True:
                count = count + 1
    return count


def change_direction(matrix, bool_matrix, guard_x, guard_y, num_row, num_column, dir):
    # 1 --> UP
    # 2 --> RIGHT
    # 3 --> SUD
    # 4 --> EST
    if dir == 1:
        return step_right(matrix, bool_matrix, guard_x, guard_y, num_row, num_column)
    if dir == 2:
        return step_down(matrix, bool_matrix, guard_x, guard_y, num_row, num_column)
    if dir == 3:
        return step_left(matrix, bool_matrix, guard_x, guard_y, num_row, num_column)
    if dir == 4:
        return step_up(matrix, bool_matrix, guard_x, guard_y, num_row, num_column)


def step_up(matrix, bool_matrix, guard_row, guard_column, num_row, num_column):
    print('UP')
    print('currently in ' + str(guard_row) + ' ' + str(guard_column))
    bool_matrix[guard_row][guard_column] = True
    if guard_row == 0:
        return count_step(bool_matrix, num_row, num_column)
    else:
        if matrix[guard_row-1][guard_column] == '#':
            print('found # in ' + str(guard_row) + ' ' + str(guard_column))
            return change_direction(matrix, bool_matrix, guard_row, guard_column, num_row, num_column, 1)
        else:
            return step_up(matrix, bool_matrix, (guard_row-1), guard_column, num_row, num_column)


def step_right(matrix, bool_matrix, guard_row, guard_column, num_row, num_column):
    print('RIGHT')
    print('currently in ' + str(guard_row) + ' ' + str(guard_column))
    bool_matrix[guard_row][guard_column] = True
    if guard_column == (num_column - 1):
        return count_step(bool_matrix, num_row, num_column)
    else:
        if matrix[guard_row][guard_column+1] == '#':
            print('found # in ' + str(guard_row) + ' ' + str(guard_column))
            return change_direction(matrix, bool_matrix, guard_row, guard_column, num_row, num_column, 2)
        else:
            return step_right(matrix, bool_matrix, guard_row, (guard_column+1), num_row, num_column)


def step_down(matrix, bool_matrix, guard_row, guard_column, num_row, num_column):
    print('DOWN')
    print('currently in ' + str(guard_row) + ' ' + str(guard_column))
    bool_matrix[guard_row][guard_column] = True
    if guard_row == (num_row - 1):
        return count_step(bool_matrix, num_row, num_column)
    else:
        if matrix[guard_row+1][guard_column] == '#':
            print('found # in ' + str(guard_row) + ' ' + str(guard_column))
            return change_direction(matrix, bool_matrix, guard_row, guard_column, num_row, num_column, 3)
        else:
            return step_down(matrix, bool_matrix, (guard_row+1), guard_column, num_row, num_column)


def step_left(matrix, bool_matrix, guard_row, guard_column, num_row, num_column):
    print('LEFT')
    print('currently in ' + str(guard_row) + ' ' + str(guard_column))
    bool_matrix[guard_row][guard_column] = True
    if guard_column == 0:
        return count_step(bool_matrix, num_row, num_column)
    else:
        if matrix[guard_row][guard_column-1] == '#':
            print('found # in ' + str(guard_row) + ' ' + str(guard_column))
            return change_direction(matrix, bool_matrix, guard_row, guard_column, num_row, num_column, 4)
        else:
            return step_left(matrix, bool_matrix, guard_row, (guard_column-1), num_row, num_column)



with open('Day6\\input_Day6.txt') as file:
    input = file.read()
    matrix = input.split('\n')

num_row = len(matrix)
num_column = len(matrix[0])

bool_matrix = [[False for k in range(num_row)] for l in range(num_column)]

position = search_guard(matrix, num_row, num_column)
guard_row = position[0]
guard_column = position[1]

ans = step_up(matrix, bool_matrix, guard_row, guard_column, num_row, num_column)

print(ans)