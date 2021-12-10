#! /usr/bin/env python3

import sys

def main():
	total = 0
	nums = []
	nums.append(int(sys.stdin.readline()))
	while (line := sys.stdin.readline()):
		nums.append(int(line))
		if len(nums) == 4:
			if nums[3] > nums[0]:
				total += 1
			nums.pop(0)

	print(total)
		

if __name__ == "__main__":
	main()
