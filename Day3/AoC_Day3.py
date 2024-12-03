def check_parenthesis(input, num_start):

    length_to_end = len(input[num_start:])
    is_closing_par = False

    # I search a closing parenthesis starting from num_start + 3 (can't be before)
    for i in range(5):
        index = i+3
        if input[num_start + index] == ')':
            is_closing_par = True
            closing_index = num_start + index
            break
    
    if not is_closing_par:
        return 0
    
    # I know that that parenthesis are in [num_start - 1] and in [closing_index]
    # So between [num_start] and [closing_index -1] there needs to be one comma and all numbers.

    # The comma needs to be and index 1, 2 or 3
    is_comma = False

    for i in range(3):
        index_adjust = i + 1
        if input[num_start + index_adjust] == ',':
            comma_index = num_start + index_adjust
            is_comma = True
            break

    if not is_comma:
        return 0
    
    # At this point i know there are opening and closing parenthesis and there is also a comma.
    # I just need to see if pre-comma and post-comma chars are all digits.

    pre_comma = check_all_digits(input, num_start, comma_index)
    post_comma = check_all_digits(input, (comma_index + 1), closing_index)
    return pre_comma * post_comma


def check_all_digits(input, start, end):
    sliced_string = input[start:end]
    all_digits = sliced_string.isdigit()

    num = 0

    if all_digits:
        num = int(sliced_string)

    return num




with open('Day3\\input_Day3.txt') as file:
    input = file.read()

ans = 0

for c in range(len(input) - 5):
    if input[c:(c+4)] == 'mul(':
        ans_molt = check_parenthesis(input, (c+4))
        ans = ans + ans_molt
        
print(ans)

