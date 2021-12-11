#! /usr/bin/env python3

import sys

def calc_fuel(x1, x2):
	return (abs(x1 - x2) * (abs(x1 - x2)+1)) // 2

def main():
	crabs = list(map(int, sys.stdin.readline().strip().split(',')))		
	minFuel = sys.maxsize

	minS = min(crabs)
	maxS = max(crabs)

	for spot in range(minS, maxS):
		fuel = [calc_fuel(crab, spot) for crab in crabs]
		minFuel = min(minFuel, sum(fuel))

	print(minFuel)


if __name__ == "__main__":
	main()
