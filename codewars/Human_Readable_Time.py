# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):

	time = ''
	while(time.count(':') < 2):

		seconds,s = divmod(seconds,60)
		time = ':%02d' % s + time

	time = '%02d' % seconds + time

	return time

def make_readable_clever(seconds):

	return '{:02}:{:02}:{:02}'.format(seconds / (60 * 60),seconds / 60 % 60,seconds % 60)

print make_readable_clever(359999)