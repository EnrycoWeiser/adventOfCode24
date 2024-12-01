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

####### PART 2 #######
sum2 = 0

for i in range (len(left)):
    repeat = right.count(left[i])
    ans2 = repeat * int(left[i])
    sum2 = sum2 + ans2

print(sum2)



