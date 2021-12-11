#! /usr/bin/env python3

import sys

SIZE = 10
LENGTH = 200


def read_input():
	octopi = []
	octopi.append([0] * (SIZE+2))
	while line := sys.stdin.readline().strip():
		row = [i for i in list(line)]
		row = [0] + row + [0]
		octopi.append(list(map(int, row)))
		

	octopi.append([0] * (SIZE+2))
	return octopi

def update(octopi):
	for i in range(1, SIZE+1):
		for j in range(1, SIZE+1):
			octopi[i][j] += 1

def spread(octopi, i, j):
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):
			if y == 0 and x == 0:
				continue
				
			if octopi[i+x][j+y] != 0:
				octopi[i+x][j+y] += 1

def flash(octopi):
	isFlash = True

	flashes = 0
	while isFlash:
		isFlash = False
		for i in range(1, SIZE+1):
			for j in range(1, SIZE+1):
				#print(octopi[i][j])
				if octopi[i][j] > 9:
					flashes += 1
					octopi[i][j] = 0
					spread(octopi, i, j)
					isFlash = True

	return flashes
	

def print_octo(octopi):
	for i in range(1, SIZE+1):
		for j in range(1, SIZE+1):
			print(octopi[i][j],end="")

		print("")

	print("")

def main():
	octopi = read_input()
	flashes = 0

	print_octo(octopi)
	step = 1
	while True:
		update(octopi)
		flashes += flash(octopi)
		if sum([sum(i) for i in octopi]) == 0:
			print(step)
			break
		print(f'step {step+1}')
		step += 1
		print_octo(octopi)

	print(flashes)

if __name__ == "__main__":
	main()
