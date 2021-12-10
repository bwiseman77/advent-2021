#! /usr/bin/env python3

import sys

SIZE = 1000

graph = [[0] * SIZE for _ in range(SIZE)]

def read_points():
	p = []
	while line := sys.stdin.readline():
		x, z, y = line.split()
		p.append(list(map(int, (x.split(',') + y.split(',')))))

	return p

def mark_graph(line, graph):

	x1, y1, x2, y2 = line

	dx = 1
	dy = 1
	if x1 > x2:
		dx = -1
	
	if x1 == x2:
		dx = 0

	if y1 > y2:
		dy = -1

	if y1 == y2:
		dy = 0


	while x1 != x2 or y1 != y2:
		graph[x1][y1] += 1
		x1 += dx
		y1 += dy

	graph[x1][y1] += 1

def calc_graph(graph):
	score = 0
	
	for i in range(SIZE):
		for j in range(SIZE):
			if graph[i][j] >= 2:
				score += 1

	return score

def print_graph(graph):
	for row in graph:
		print(row)

def main():

	points = read_points()

	for line in points:
		mark_graph(line, graph)

	score = calc_graph(graph)
	print(score)

if __name__ == "__main__":
	main()
