with open ('Day1\input_Day1.txt') as file:
    input = file.read().strip()
    lines = input.split('\n')

left = []
right = []

for l in lines:
    line = l.split('   ')
    left.append(line[0])
    right.append(line[1])

left.sort()
right.sort()

sum = 0

for i in range(len(left)):
    diff = int(left[i])-int(right[i])
    ans = abs(diff)
    sum = sum + ans

print(sum)
