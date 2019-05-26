# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# JavaScript:

# seven(times(five())); // must return 35
# four(plus(nine())); // must return 13
# eight(minus(three())); // must return 5
# six(dividedBy(two())); // must return 3
# Ruby:

# seven(times(five)) # must return 35
# four(plus(nine)) # must return 13
# eight(minus(three)) # must return 5
# six(divided_by(two)) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...


# def zero(para=()): #your code here

# 	if para == ():

# 		return 0

# 	else:

# 		a,b = para
# 		return eval('0' + a + str(b))


# def one(para=()): #your code here

# 	if para == ():

# 		return 1

# 	else:

# 		a,b = para
# 		return eval('1' + a + str(b))

# def two(para=()): #your code here

# 	if para == ():

# 		return 2

# 	else:

# 		a,b = para
# 		return eval('2' + a + str(b))

# def three(para=()): #your code here

# 	if para == ():

# 		return 3

# 	else:

# 		a,b = para
# 		return eval('3' + a + str(b))

# def four(para=()): #your code here

# 	if para == ():

# 		return 4

# 	else:

# 		a,b = para
# 		return eval('4' + a + str(b))

# def five(para=()): #your code here

# 	if para == ():

# 		return 5

# 	else:

# 		a,b = para
# 		return eval('5' + a + str(b))

# def six(para=()): #your code here

# 	if para == ():

# 		return 6

# 	else:

# 		a,b = para
# 		return eval('6' + a + str(b))

# def seven(para=()): #your code here

# 	if para == ():

# 		return 7

# 	else:

# 		a,b = para
# 		return eval('7' + a + str(b))

# def eight(para=()): #your code here

# 	if para == ():

# 		return 8

# 	else:

# 		a,b = para
# 		return eval('8' + a + str(b))

# def nine(para=()): #your code here

# 	if para == ():

# 		return 9

# 	else:

# 		a,b = para
# 		return eval('9' + a + str(b))

# def plus(n): #your code here

# 	return '+',n

# def minus(n): #your code here

# 	return '-',n

# def times(n): #your code here

# 	return '*',n

# def divided_by(n): #your code here

# 	return '/',n

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y