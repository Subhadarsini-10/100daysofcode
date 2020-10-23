#give 2 inputs x and y and then create a 2 dimentional array.

input_for_system = input()
dimension = [int(x) for x in input_for_system.split(',')]
rowin = dimension[0]
colsin = dimension[1]
list = [[0 for column in range(colin)] for row in range(rowin)]

for row in range(rowin):
    for column in range(colin):
        list[row][col] = row*col
print[list]