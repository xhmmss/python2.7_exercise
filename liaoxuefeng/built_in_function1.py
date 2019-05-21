print abs(-888)

print all(['a','b']) #[] or ()
print all(['a',''])
print all([1,2])
print all([0,1])
print all([])
print all(())

print any([0,'',False])
print any(())
print any([])

print isinstance("Hello",(str,unicode))
print isinstance("Hello",basestring)
print bin(15)

print bool()
print bool(0)
print bool('0')
print issubclass(bool,int)

print bytearray(5)
print bytearray("abcd","utf-8")
print bytearray([1,2,3])

print callable(bool)

print chr(0x30)

class A(object):
	bar = 1
	def func1(self):
		print "func1"
	@classmethod
	def func2(cls):
		print "func2"

A.func2()

print cmp(1,11)
print cmp(1,1)
print cmp(11,1)

print compile("for i in range(10): print i",'','exec')
exec(compile("for i in range(10): print i",'','exec'))

print complex(1,2)

delattr(A,'bar')

print dict(a='1',b='2')
print dict([('a',1),('b',2)])

print dir()
print dir([])