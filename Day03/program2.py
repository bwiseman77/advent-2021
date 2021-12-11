#! /usr/bin/env python3

import sys

def remove(codes, bit, n):
	Ncodes = []
	for code in codes:
		if code[bit] == n:	
			Ncodes.append(code)

	return Ncodes

def main():
	line = sys.stdin.readline().strip()
	l = len(line)
	bits = [0] * l
	CODES = []

	while line:
		CODES.append(line)
		line = sys.stdin.readline().strip()

	codes = CODES.copy()

	for index in range(len(bits)):
		total = len(codes)
		if len(codes) == 1:
			continue

		for code in codes:
			if code[index] == '1':
				bits[index] += 1
	
		if bits[index] >= total / 2:
			codes = remove(codes, index, '1')

		else:
			codes = remove(codes, index, '0')


	Ocodes = CODES.copy()
	bits = [0] * l
	
	for index in range(len(bits)):
		total = len(Ocodes)
		if len(Ocodes) == 1:
			continue

		for code in Ocodes:
			if code[index] == '1':
				bits[index] += 1

		print(bits[index], total)
		if bits[index] >= total / 2:
			Ocodes = remove(Ocodes, index, '0')
		else:
			Ocodes = remove(Ocodes, index, '1')

		print(Ocodes)
	
	print(codes[0], Ocodes[0])
	O = int("".join(map(str, codes[0])), 2)
	C = int("".join(map(str, Ocodes[0])), 2)
	print(O, C, O * C)



if __name__ == "__main__":
	main()
