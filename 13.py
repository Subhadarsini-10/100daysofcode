#password check
import re
p = input('Enter a password')
x = True

while x:
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search('[a-z]', p):
        break
    elif not re.search('[0-9]', p):
        break
    elif not re.search('[A-Z]', p):
        break
    elif not re.search('[#$@]', p):
        break
    else:
        print('password check gives a green line')
        x = False
        break
if x:
    print('x is bs password-you are banned for life')



#even_digits
even_digits = []
for i in range(200, 401):
    s = str(i)
    if (int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0):
        even_digits.append(s)
print('$'.join(even_digits))


#create a program that prints a letter A.

letter_A = ''
for row in range(0,7):
    for column in range(0,7):
    if(((column==1 or column==5) and row!=0)or ((row==0 or row==3)and (column>1 and column<5))):
        letter_A = letter_A+'*'
    else:
        letter_A = letter_A+' '
    letter_A = letter_A+'ln'
print(letter_A)