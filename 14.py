#make a grid and find out how to move the dots to the right to make it to s slot and do it for 'x' it's good pracice.
letter_s = ''
for row in range(7):
    for col in range(7):
        if((row == 0 or row == 3 or row ==6) and (col>0 and col<7)):
            letter_s = letter_s + '*'
        elif((row == 1 or row == 2) and (col == 1)):
            letter_s = letter_s + '*'
        elif((row == 4 or row == 5) and (col == 6)):
            letter_s = letter_s + '*'
        else:
            letter_s = letter_s + ' '
    letter_s = letter_s + '\n'
print(letter_s)

#else do the same for 'x'

i = ''
for row in range(0,7):
    for col in range(0,7):
        if((row == 0 or row == 6) and (col>0 and col<8)):
            i = i +'*'
        elif((row == 1 or row == 1 or row == 2 or row == 3 or row == 4 or row ==5 or row == 6) and (col == 3)):
            i = i +'*'
        else:
            i = i + ' '
    i = i + '\n'
print(i)

#py progarm which the age in dog years.
#dog year 0-2 = 10.5 years in human age.
#after that each dog year = 4 human years.

human = int(input('how many human years the dog been alive'))
if human <0:
    print('the input must be a positive integer')
    exit()
elif(human<=2):
    dog_age = human*10.5
else:
    dog_age = 21 + (human-2)*4
print("The dog's age in dog's year is:",dog_age)

#write a program to check whether it is a vowel or a consonent.

x = input('use any letter from the alphabet')
if x in ('a', 'e', 'i', 'o', 'u'):
    print('{} is a vowel', format(x))
elif x == 'y':
    print('A, E, I, O, U and sometimes Y')
else:
    print('{} is a consonent', format(x))


#give me a month and i'll share u the no. of days is consist of.
month = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
         'november', 'december')
print('lists of months:', month)
month = input('give me a month')
if month == 'february':
    print('consist of 28/29 days')
elif month in ('april', 'june', 'november', 'september'):
    print('consist of 30 days')
elif month in ('january', 'march', 'may', 'july', 'august', 'october', 'december'):
    print('consist of 31 days')
else:
    print('Enter a valid month')

#allow 2 inputs,day and month and program can split out season.
month = input("enter any month")
day = int(input('enter any numerical day'))

x = ('january', 'february', 'march')
y = ('april', 'may', 'june')
z = ('july', 'august', 'september')

if month in (x):
    season = "winter"
elif month in (y):
    season = 'summer'
elif month in (z):
    season = 'rainy'
else:
    season = 'autumn'

if((month == 'march') and (day>19)):
    season = 'spring'
elif((month == 'june') and (day>20)):
    season = 'summer'
elif((month == 'september') and (day>21)):
    season = 'autumn'
elif((month == 'december') and (day>19)):
    season = 'winter'

print('season is:', season)


# write a program to find the median of 3 values.
a = int(input('first number:'))
b = int(input('sec number:'))
c = int(input('third number:'))

if a>b:
    if a<c:
        median = a
    elif b>c:
        median = b
    else:
        median = c
else:
    if a>c:
        median = a
    elif b<c:
        median = b
    else:
        median = c
print('median:', median)