# Easy level, Lowercase challenge
# https://www.codeeval.com/open_challenges/20/

__author__ = 'EmilioK'

import sys


def main(argv):
	f = open(argv[1])
	for line in f.readlines():
		print line.lower()

if __name__ == '__main__':
	main(sys.argv)

