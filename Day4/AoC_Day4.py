def search_line_forward(input):
    count = 0
    for c in range(len(input) - 3):
        if input[c : (c+4)] == 'XMAS':
            count = count + 1
    return count


def search_line_backward(input):
    count = 0
    for c in range(len(input) - 3):
        if input[c : (c+4)] == 'SAMX':
            count = count + 1
    return count


def search_vertical_down(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if splitted[row][char] == 'X' and splitted[row+1][char] == 'M' and splitted[row+2][char] == 'A' and splitted[row+3][char] == 'S' :
                    count = count + 1
    return count


def search_vertical_up(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if splitted[row][char] == 'S' and splitted[row+1][char] == 'A' and splitted[row+2][char] == 'M' and splitted[row+3][char] == 'X' :
                    count = count + 1   
    return count


def search_diagonal_nw_se(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if char >= (len(splitted[row]) - 3):
                    continue
                if splitted[row][char] == 'X' and splitted[row+1][char+1] == 'M' and splitted[row+2][char+2] == 'A' and splitted[row+3][char+3] == 'S' :
                    count = count + 1
    return count

def search_diagonal_se_nw(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if char >= (len(splitted[row]) - 3):
                    continue
                if splitted[row][char] == 'S' and splitted[row+1][char+1] == 'A' and splitted[row+2][char+2] == 'M' and splitted[row+3][char+3] == 'X' :
                    count = count + 1
    return count

def search_diagonal_ne_sw(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if char <= 2:
                    continue
                if splitted[row][char] == 'X' and splitted[row+1][char-1] == 'M' and splitted[row+2][char-2] == 'A' and splitted[row+3][char-3] == 'S' :
                    count = count + 1
    return count

def search_diagonal_sw_ne(splitted):
    count = 0
    lines_number = len(splitted)

    for row in range(lines_number):
        if row >= (lines_number - 3):
            continue
        else:
            for char in range(len(splitted[row])):
                if char <= 2:
                    continue
                if splitted[row][char] == 'S' and splitted[row+1][char-1] == 'A' and splitted[row+2][char-2] == 'M' and splitted[row+3][char-3] == 'X' :
                    count = count + 1
    return count

def search_x_mas(splitted):
    count = 0
    lines_numbers = len(splitted)
    for row in range(lines_numbers):
        # The As can't be on first or last row
        if row == 0 or row == (lines_numbers - 1):
            continue
        else:
            char_numbers = len(splitted[row])
            for char in range(char_numbers):
                # The As can't be on first or last column
                if char == 0 or char == (char_numbers - 1):
                    continue
                if splitted[row][char] == 'A':
                    # Check the first diag (NW to SE)
                    first_diag = False
                    if (splitted[row-1][char-1] == 'M' and splitted[row+1][char+1] == 'S') or (splitted[row-1][char-1] == 'S' and splitted[row+1][char+1] == 'M'):
                        first_diag = True
                    # Check the second diag (NE to SW)
                    second_diag = False
                    if (splitted[row-1][char+1] == 'M' and splitted[row+1][char-1] == 'S') or (splitted[row-1][char+1] == 'S' and splitted[row+1][char-1] == 'M'):
                        second_diag = True
                    if first_diag and second_diag:
                        count = count + 1
    return count


with open('Day4\\input_Day4.txt') as file:
    input = file.read()
    splitted = input.split('\n')

line_forward = search_line_forward(input)
line_backward = search_line_backward(input)

vertical_up = search_vertical_up(splitted)
vertical_down = search_vertical_down(splitted)

diagonal_ne_sw = search_diagonal_ne_sw(splitted)
diagonal_sw_ne = search_diagonal_sw_ne(splitted)

diagonal_nw_se = search_diagonal_nw_se(splitted)
diagonal_se_nw = search_diagonal_se_nw(splitted)

print(line_forward + line_backward + vertical_down + vertical_up + diagonal_ne_sw + diagonal_sw_ne + diagonal_nw_se + diagonal_se_nw)

x_mas = search_x_mas(splitted)

print(x_mas)