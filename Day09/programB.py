#! /usr/bin/env python3

import sys

LENGTH = 10

def read_map():
	#Map = [[10] * (LENGTH + 2)]
	Map = []
	while line := sys.stdin.readline().strip():
		row = [int(i) for i in list(line)]
		row = [10] + row + [10]
		Map.append(row)

	h = len(Map)
	w = len(Map[0])

	Map.insert(0, [10] * w)
	Map.append([10] * w)


	#Map.append([10] * (LENGTH + 2))

	return Map

def pmap(Map):
	for line in Map:
		print(line)

def check_adj(Map, x, y):
	u = Map[x][y+1]
	d = Map[x][y-1]
	l = Map[x-1][y]
	r = Map[x+1][y]
	s = Map[x][y]

	if u <= s or d <= s or l <= s or r <= s:
		return 0

	print(s)
	return s + 1

def check_map(Map):
	lowPoints = []
	risk = 0
	for i in range(1, len(Map[0]) - 1):
		for j in range(1, len(Map) - 1):
			r = check_adj(Map, j, i)
			if r > 0:
				risk += r
				lowPoints.append((j, i))
			
	
	return risk, lowPoints

def find_basin(Map, lowPoints):
	sizes = []
	for point in lowPoints:
		size = 0
		froniter = [point]
		visited = set()

		while froniter:
			x, y = froniter.pop(0)
	
			if (x, y) in visited:
				continue

			visited.add((x, y))
			if Map[x][y] < 9:
				size += 1


			if Map[x][y] < 9:
				froniter.append((x+1, y))
				froniter.append((x-1, y))
				froniter.append((x, y+1))
				froniter.append((x, y-1))

		sizes.append(size)

	return sizes

def main():
	Map = read_map()
	pmap(Map)
	risk, lowPoints = check_map(Map)
	print(risk, lowPoints)
	sizes= find_basin(Map, lowPoints)
	s = sorted(sizes, reverse=True)[0:3]
	print(s[0] * s[1] * s[2])

if __name__ == "__main__":
	main()
