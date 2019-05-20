# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

# Examples:
# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
# tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)

def tickets(people):

	cash = []

	for p in people:

		if p == 25:

			cash.append(p)

		elif p == 50:

			if 25 in cash:

				cash.remove(25)
				cash.append(p)

			else:

				return "NO"

		elif p == 100:

			if (cash.count(25) > 0 and cash.count(50) > 0) or (cash.count(25) > 2):

				if cash.count(50) > 0:

					cash.remove(25)
					cash.remove(50)
					cash.append(p)

				else:

					cash.remove(25)
					cash.remove(25)
					cash.remove(25)
					cash.append(p)

			else:

				return "NO"

	return "YES"

def  tickets_clever1(people):

	n25 = n50 = 0

	for p in people:
		if p == 25:
			n25 += 1
		elif p == 50:
			n50 += 1
			n25 -= 1
		elif p == 100 and n50 > 0:
			n50 -= 1
			n25 -= 1
		elif p == 100 and n50 == 0:
			n25 -= 3
		if n25 < 0 or n50 < 0:
			return "NO"
	return "YES"


print tickets([25, 25, 50, 50, 100])