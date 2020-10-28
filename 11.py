#write a program iterating frmo 0 to 50, if num is a multiple of 3 then print supaa instead of num,elif  num is multipla of
#of a  print badass, if num is multiple of both print super badass.

for i in range(0,50):
    if(i%3 == 0):
        print('SUPPA')
    elif(i%5 == 0):
        print('BADASS')
    elif(i%3 == 0 and i%5 == 0):
        print('SUPPA BADASS')
    else:
        print(i)

#take 2 digits (m and n ,row and column respectively) as inputs and generates a 2d array.
# the element value in the ith row and jth column of the array should be i*j.

row_num = int(input('How many rows:'))
col_num = int(input('how many column:'))

for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row*col

print(list, '\n')


#write a program that accepts a sentance in lower case an dgive the output as(all char in uppercase).

lines = []
while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break
for line in lines:
    print(line)
