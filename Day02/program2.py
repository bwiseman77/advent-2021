#! /usr/bin/env python3

import sys

def main():
	pos = 0
	depth = 0
	aim = 0

	while(line := sys.stdin.readline()):
		direction, value = line.split()
		value = int(value)
		if direction == "forward":
			pos += value
			depth += (value * aim)
		elif direction == "up":
			aim -= value
		elif direction == "down":
			aim += value


	total = pos * depth
	print(total)

if __name__ == "__main__":
	main()
