#! /usr/bin/env python3

import sys

def main():
	total = 0
	start = int(sys.stdin.readline())
	while (line := sys.stdin.readline()):
		if int(line) > start:
			total += 1
		start = int(line)

	print(total)
		

if __name__ == "__main__":
	main()
