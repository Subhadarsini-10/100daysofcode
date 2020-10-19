#create a class the includes 2 methods.
#getstring = grab string from input
#printstring = print the string in uppercase

class me(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input('give me a string')
    def printString(self):
        print(self.s.upper())

x = me()
print(x)

x.getString()
x.printString()