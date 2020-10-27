from array import *
array_num = {'i', [1,3,4,6]}
for i in array_num:
    print(i)
print('access the first three items')
print(array_num[0])
print(array_num[1])
print(array_num[2])

print('starting array', array_num)
array_num.append(11)
print('new array', array_num)

print(array_num[::-1])

print(array_num)
array_num.insert(2,4)
print('new array', array_num)

array_num.pop(3)
print(array_num)

print(type(new_array))
x = new_array.tolist()
print(type(x))