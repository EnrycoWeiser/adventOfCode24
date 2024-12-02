def check_order(a) -> bool:

    order_asc = True
    order_desc = True

    # check ascending
    for i in range(len(a) - 1):
        if int(a[i]) >= int(a[i+1]):
            order_asc = False
            break

    # check descending
    if not order_asc:
        for j in range(len(a) - 1):
            if int(a[j]) <= int(a[j+1]):
                order_desc = False
                break

    if order_asc:
        return check_asc_step(a)
    if order_desc:
        return check_desc_step(a)
    else:
        return False    

def check_asc_step(line) -> bool:
    for z in range(len(line) - 1):
        if int(line[z]) + 3 < (int(line[z+1])):
            return False
    return True

def check_desc_step(line) -> bool:
    for x in range(len(line) - 1):
        if int(line[x]) - 3 > (int(line[x+1])):
            return False
    return True

#     #             #       #
####### END METHODS #########
#     #             #       #

with open('Day2\\input_Day2.txt') as file:
    input = file.read().strip()
    lines = input.split('\n')

count = 0
unsafe = []

for l in lines:
    line = l.split(' ')
    if check_order(line):
        count = count + 1
    else:
        unsafe.append(line)
    

#print(count)


####### PART 2 #######


count2 = 0

for u in unsafe:
    for h in range(len(u)):
        new_u = u.copy()

        new_u.pop(h)

        if check_order(new_u):
            count2 = count2 + 1
            break
        
print(count + count2)