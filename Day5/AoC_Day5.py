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
for seq in sequences:
    mid = find_mid(seq)
    is_correct = check_seq(seq, pipes)

    if is_correct:
        sum = sum + int(mid)

print(sum)