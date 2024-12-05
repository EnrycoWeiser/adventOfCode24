def check_seq(sequence, pipes):
    length = len(sequence)
    if length == 1:
        return True

    for pipe in pipes:
        if pipe[1] == sequence[0] and pipe[0] in sequence:
            return False

    sequence.pop(0)
    return check_seq(sequence, pipes)
    
def find_mid(sequence):
    length = len(sequence)
    return sequence[int((length - 1) / 2)]

def fix_seq(sequence, pipes, deleted):
    # I need to order only the first half of the sequence
    print(sequence)
    is_mid = False
    length = len(sequence)
    if (deleted+1) == length:
        is_mid = True

    is_correct = True
    for pipe in pipes:
        if pipe[1] == sequence[0] and pipe[0] in sequence:
            print(pipe[1] + ' cant be before ' + pipe[0])
            sequence.append(sequence[0])
            sequence.pop(0)
            is_correct = False
            break
    
    if not is_correct:
        return fix_seq(sequence, pipes, deleted)
    elif is_mid:
        print('is mid')
        return sequence[0]
    else:
        print('removed ' + sequence[0] + ' in the correct pos')
        sequence.pop(0)
        deleted = deleted + 1

    print(sequence)

    return fix_seq(sequence, pipes, deleted)


with open('Day5\\input_Day5.txt') as file:
    input = file.read()
    split = input.split('\n\n')
    
pipes_all = split[0].split('\n')
sequences_all = split[1].split('\n')

pipes = []
sequences = []

for line in pipes_all:
    pipes_split = line.split('|')
    pipes.append([pipes_split[0], pipes_split[1]])

for line in sequences_all:
    sequences_split = line.split(',')
    pre_seq = []
    for num in sequences_split:
        pre_seq.append(num)
    sequences.append(pre_seq)

sum = 0
not_correct = []

for seq in sequences:
    new_seq = seq.copy()
    mid = find_mid(seq)
    is_correct = check_seq(seq, pipes)

    if is_correct:
        sum = sum + int(mid)
    else:
        not_correct.append(new_seq)

####### PART 2 #######

sum_nc = 0
for nc in not_correct:
    ans_nc = fix_seq(nc, pipes, 0)
    sum_nc = sum_nc + int(ans_nc)

print(sum_nc)
