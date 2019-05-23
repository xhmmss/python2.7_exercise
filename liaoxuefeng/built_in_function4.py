f = open('built_in_function1.py')
f.close()

print ord('A')

print pow(2,2)

class Shuxing():
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)
sx = Shuxing(100)
print sx.x
sx.x = 106
print sx.x
del sx.x

print reduce(lambda x,y: x+y,[1,2,3,4])

import sys
reload(sys)

dict = {'runoob': 'runoob.com', 'google': 'google.com'}
print repr(dict)

print round(80.123456,4)

print set('aaaa')

a = range(10)
print a[slice(5)]

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print sorted(students, key=lambda s: s[2]) 

print tuple([1,2,3,4])

print range(10)
print xrange(10)
print list(xrange(10))

print zip([1,2,3],['a','b','c'])