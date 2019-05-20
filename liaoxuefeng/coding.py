# coding:utf-8
# All language in Unicode(two bytes,ASCII is a byte).
# UTF-8 is coding of variable length.


string1 = u'中文'.encode('utf-8')
print len(string1),string1

string2 = 'ABC'.decode('utf-8')
print len(string2),string2

print "%3d" % 3
print "%03d" % 3

print "%s" % 3 # %s is always worked.

print u"%s" % u"hello"

print "%% %d" % 5