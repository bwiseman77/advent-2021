#! /usr/bin/env python3

import sys

def main():
	line = sys.stdin.readline().strip()
	l = len(line)
	bits = [0] * l
	total = 1
	gamma = [0] * l
	epsilon = [0] * l

	while line:
		for index, bit in enumerate(line):
			if bit == '1':
				bits[index] += 1
		total += 1
		line = sys.stdin.readline().strip()


	for index, bit in enumerate(bits):
		if bit > (total // 2):
			gamma[index] = 1
		else:
			epsilon[index] = 1
	
	gamma = int("".join(map(str, gamma)), 2)
	epsilon = int("".join(map(str, epsilon)), 2)

	print(gamma, epsilon, epsilon*gamma)


if __name__ == "__main__":
	main()
