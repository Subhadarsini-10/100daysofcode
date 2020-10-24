#common basics

pets = ['cat', 'dog', 'monkey', 'fish']
print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])

#for loop
for names in pets:
    print(names)

#while loop
i_got_money = 20
while i_got_money < 25:
    print(i_got_money)
    i_got_money += 1

print('i need more money')

for i in range(100, 110):
    if(i%7==0 and i%5==0):
        print(i)
#game
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10, and keep guessing till you got'))
print('game over')

#count
count = 0
for i in range(7):
    count += 1
    print('.' + count)
for num in range(6):
    count += 1
    print('.' + count)