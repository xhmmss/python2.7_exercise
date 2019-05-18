# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:

# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):

	array = [int(i) for i in numbers.split(' ')]
	numbers = "" + str(max(array)) + " " + str(min(array))

	return numbers

def high_and_low-clever(numbers):

	array = [int(i) for i in numbers.split(' ')]

	return "%s %s" % (max(array),min(array))

print high_and_low("1547 294 2059 127 577 3208 1479 1716 220 1417 1828 2317 248 2137 306 2363 2745 314 1273 2049 1472 865")