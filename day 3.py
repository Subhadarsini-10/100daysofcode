#given integral n ,create a dictionary with function that creates  a key reslut.
print('enter a number')
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i

print(d)