#! /usr/bin/env python3

import sys

NEW = 8
RESET = 6
DONE = 0
DAYS = 256

def check_fish(fishes):
	for index, fish in enumerate(fishes):
		if fish < DONE:
			fishes[index] = RESET
			fishes.append(NEW)

def dday(fishes):
	for index, fish in enumerate(fishes):
		fishes[index] -= 1

def main():
	fishes = list(map(int, sys.stdin.readline().strip().split(',')))

	print(f'initial: {fishes}')
	for i in range(DAYS):
		dday(fishes)
		check_fish(fishes)
		#print(f'After {i+1} days: {fishes}')

	print(len(fishes))



if __name__ == "__main__":
	main()
