# print input("input:")

print int(3.6)
print int('12',16)

a = 2
print isinstance(a,int)

class A:
	pass
class B(A):
	pass
print issubclass(B,A)

l = [1,2,3,4,5]
it = iter(l)
print next(it)

print len(l)

t = (1,'2',3,'4')
print list(t)

print locals()

print long('123')

print map(lambda x: x + 2,l)

print max(l)
print min(l)

v = memoryview('abcdefg')
print v[1],v[1:4],v[1:4].tobytes()

print oct(8)