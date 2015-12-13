# Easy level, Morse code challenge
# https://www.codeeval.com/open_challenges/116/

__author__ = 'EmilioK'

import sys


def main(argv):

	morse_dict = {
		'.-': 'A', '-...': 'B', '-.-.': 'C',
		'-..': 'D', '.': 'E', '..-.': 'F',
		'--.': 'G', '....': 'H', '..': 'I',
		'.---': 'J', '-.-': 'K', '.-..': 'L',
		'--': 'M', '-.': 'N', '---': 'O',
		'.--.': 'P', '--.-': 'Q', '.-.': 'R',
		'...': 'S', '-': 'T', '..-': 'U',
		'...-': 'V', '.--': 'W', '-..-': 'X',
		'-.--': 'Y', '--..': 'Z', '.----': '1',
		'..---': '2', '...--': '3', '....-': '4',
		'.....': '5', '-....': '6',  '--...': '7',
		'---..': '8', '----.': '9', '-----': '0'
	}

	f = open(argv[1])

	for line in f.readlines():
		# Clear line buffer after the line print
		decoded_line = ''

		for char in line.split(' '):
			# If the char is empty it means that the character is an space
			if char == '':
				decoded_line += ' '
			else:
				# If isn't empty is a morse character, lets cross it with our morse_dict
				decoded_line += morse_dict[char.replace('\n', '')]
		print decoded_line

if __name__ == '__main__':
	main(sys.argv)
