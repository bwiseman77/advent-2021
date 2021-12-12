#! /usr/bin/env python3

import sys
import collections

OPEN = ('(', '{', '[', '<')

SIGNS = {')' : '(',
		'}' : '{',
		']' : '[',
		'>' : '<'
		}

SCORE = {'(' : 1,
		'[' : 2,
		'{' : 3,
		'<' : 4
		}

def calc_score(stack):
	score = 0
	for bracket in reversed(stack):
		score *= 5
		score += SCORE[bracket]

	return score
	
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
				return 0

	return calc_score(stack) 

def main():
	scores = []
	
	while line := sys.stdin.readline().strip():
		chunks = list(line)
		s = find_corrupt(chunks)
		if s != 0:
			scores.append(s)

	print(sorted(scores)[len(scores)//2])

if __name__ == "__main__":
	main()
