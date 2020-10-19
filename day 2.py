#compute the factorial of a given number,result printed in a single line

def factorial(num):
    if (num==0):
        return 1
    return num*factorial(num-1)
print('enter an integer')
num=int(input())
print(factorial(num))

