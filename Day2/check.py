with open('Day2\\check.txt') as file1:
    input1 = file1.read()
    input1_all = input1.split('\n')

with open('Day2\\file2.txt') as file2:
    input2 = file2.read()
    input2_all = input2.split('\n')

for i in range(1000):
    if input1_all[i] != input2_all[i]:
        print('Error in ' + str(i))