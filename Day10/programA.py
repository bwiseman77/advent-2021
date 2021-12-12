#! /usr/bin/env python3

import sys

OPEN = ('(', '{', '[', '<')

SIGNS = {')' : '(',
		'}' : '{',
		']' : '[',
		'>' : '<'
		}

SCORE = {')' : 3,
		']' : 57,
		'}' : 1197,
		'>' : 25137
		}

def find_corrupt(chunks):
	stack = []

	for bracket in chunks:

		# is an open bracket
		if bracket in OPEN:
			stack.append(bracket)
			
		# is a closing bracket
		else:
			b = stack.pop(-1)
			if b != SIGNS[bracket]:
				return SCORE[bracket]

	return 0 

def main():
	score = 0
	
	while line := sys.stdin.readline().strip():
		chunks = list(line)
		score += find_corrupt(chunks)

	print(score)

if __name__ == "__main__":
	main()
