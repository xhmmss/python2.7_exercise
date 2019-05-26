# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):

	score = 0

	for a in x.split(' '):

		tmp = 0

		for i in a:

			tmp += ord(i) - ord('a') + 1

		if tmp > score:

			score = tmp
			word = a 

	return word

def high_clever(x):

	return max(x.split(),key=lambda k:sum(ord(i) -96 for i in k))

print high_clever("man i need a taxi up to ubud")