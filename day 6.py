#create a cool calculator

#use the formula q=sqrt((2*c*d)/d)

c = 50
h = 30
import math
x = []
y = [i for i in input('give me a number').split(',')]
for d in y:
    x.append((str(input((round(math.sqrt(2*c*float(d)/h)))))))
print(','.join(x))
