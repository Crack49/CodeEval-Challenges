# Easy level, Lettercase Percentage Ratio
# https://www.codeeval.com/open_challenges/147/

__author__ = 'EmilioK'

import sys


def main(argv):

	f = open(argv[1])

	for line in f.readlines():
		lower_letters = 0
		upper_letters = 0

		for char in line.strip():
			# Simple if char is lowercase checker
			if char.islower():
				lower_letters += 1
			else:
				upper_letters += 1

		# The percentage is (letters / total) * 100.0, then is the same as letters * (100.0 / total)
		total = 100.0 / (lower_letters + upper_letters)
		print 'lowercase: %.2f uppercase: %.2f' % (lower_letters * total, upper_letters * total)

if __name__ == '__main__':
	main(sys.argv)
