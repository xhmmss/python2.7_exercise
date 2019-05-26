print divmod(7,2)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print list(enumerate(seasons))

x = 7
print eval("x + 1")

execfile('data_type.py')

f = file('input_and_output.py')
print f.read()

def is_odd(n):
    return n % 2 == 1
 
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print newlist

print float(100)

print "{} {}".format('hello','world')

print frozenset(range(10))

class A(object):
	bar = 1
a = A()
print getattr(a,'bar')

print globals()

print hasattr(a,'bar')

print hash('test')

print help('sys')

print hex(255)

print id(a)