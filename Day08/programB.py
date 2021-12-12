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

def decode1(codes, num):
	for code in codes:
		#print(code)
		if len(code.strip()) == num:
			codes.remove(code)
			return set(code)

	return -1

def decode2(codes, num, ss):
	for code in codes:
		if len(code.strip()) == num:
			s = set(code)
			if ss.issubset(s):
				codes.remove(code)
				return s

def decode3(codes, num, ss):
	for code in codes:
		if len(code.strip()) == num:
			s = set(code)
			if s.issubset(ss):
				codes.remove(code)
				return s

def count_codes(back, codes):
	count = []
	for b in back:
		for i, code in enumerate(codes):
			bs = set(b)
			if set(b) == code:
				count.append(i)

	return int("".join([str(i) for i in count]))

def pcodes(codes):
	for i, code in enumerate(codes):
		print(f'{i+1}: {code}')
		

def main():
	count = 0

	while line := sys.stdin.readline().strip():
		front, back = line.split('|')
		front = front.split()
		back = back.split()
		# easy mode - uniq
		one = decode1(front, ONE)
		four = decode1(front, FOUR)
		seven = decode1(front, SEVEN)
		eight = decode1(front, EIGHT)

		# spicier
		# three = size 5 w/1
		three = decode2(front, THREE, one)
		# nine = size 6 w/3 and w/o 8
		nine = decode2(front, NINE, three)
		# zero = size 6 w/1 and w/o 3, 4, 7, 8, 9
		zero = decode2(front, ZERO, one)
		
		# extra spiicy
		# five = size 5 w/9 and w/o 8
		five = decode3(front, FIVE, nine)

		# back to easy, since everything else gone
		six = decode1(front, SIX)
		two = decode1(front, TWO)

		#pcodes((one, two, three, four, five, six, seven, eight, nine, zero))		
		count += count_codes(back, (zero, one, two, three, four, five, six, seven, eight, nine))
		

	print(count)

		
if __name__ == "__main__":
	main()
