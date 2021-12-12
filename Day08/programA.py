#! /usr/bin/env python3

import sys

ONE = 2
TWO = 5
THREE = 5
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 3
EIGHT = 7
NINE = 6
ZERO = 6

SMALL = (ONE, FOUR, SEVEN, EIGHT)

NUMS = {2 : 1,
		5 : 2,
		5 : 3,
		4 : 4,
		5 : 5,
		6 : 6,
		3 : 7,
		7 : 8,
		6 : 9, 
		6 : 0
		}

def read_outputs():
	outputs = []
	while line := sys.stdin.readline().strip():
		front, back = line.split('|')
		outputs.append(back.strip().split())

	return outputs

def main():
	count = 0

	outputs = read_outputs()


	for output in outputs:
		for code in output:
			if len(code) in SMALL:
				count += 1

	print(count)

if __name__ == "__main__":
	main()
