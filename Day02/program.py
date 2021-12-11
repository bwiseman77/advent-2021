#! /usr/bin/env python3

import sys

def main():
	pos = 0
	depth = 0

	while(line := sys.stdin.readline()):
		direction, value = line.split()
		
		if direction == "forward":
			pos += int(value)
		elif direction == "up":
			depth -= int(value)
		elif direction == "down":
			depth += int(value)


	total = pos * depth
	print(total)

if __name__ == "__main__":
	main()
