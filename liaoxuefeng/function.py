def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n

	return sum

print calc(1,2,3,4,5)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

kw = {'city': 'Beijing', 'job': 'Engineer'}

person('Jack',24,**kw)