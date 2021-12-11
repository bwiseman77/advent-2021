#! /usr/bin/env python3

import sys

NEW = 8
RESET = 6
DONE = 0
DAYS = 256


def new_day(fishes):
	babies = fishes[0]
	
	for i in range(1, len(fishes)):
		fishes[i-1] = fishes[i]

	fishes[NEW] = babies
	fishes[RESET] += babies


def main():
	fishes = [0 for i in range(NEW + 1)]

	for fish in sys.stdin.readline().strip().split(','):
		fishes[int(fish)] += 1

	for day in range(1, DAYS+1):
		new_day(fishes)
		print(fishes)

	print(sum(fishes))


if __name__ == "__main__":
	main()
