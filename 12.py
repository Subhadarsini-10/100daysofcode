lines = []
while True:
    l = input()
    if l:
        lines.append(l.lower())
    else:
        break
for l in lines:
    print(l)



# accept a string and count the no. of letters and digits it have.

s = input('give me a string:')
l, d = 0, 0
for c in s:
    if c.isalpha():
        l = l+1
    if c.isdigit():
        d = d+1
    else:
        pass
print('letters:', l)
print('digits:', d)
