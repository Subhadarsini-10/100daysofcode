#get the sum and avg of an integer number.
print('give me a number to ...type 0 to exit')

count = 0
sum = 0.0
number = 1

while number != 0:
   number = int(input())
   sum = sum+number
   count += 1

if count == 0:
    print('give me some numbers')
else:
    print('sum and average of the above numbers are:',sum, sum/(count-1))

