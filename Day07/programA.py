#! /usr/bin/env python3

import sys

def main():
	crabs = list(map(int, sys.stdin.readline().strip().split(',')))		
	spot = sorted(crabs)[len(crabs) // 2]
	print(spot)

	fuel = [abs(crab - spot) for crab in crabs]
	print(fuel, sum(fuel))
if __name__ == "__main__":
	main()
