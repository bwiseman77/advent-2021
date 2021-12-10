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

	if x1 > x2:
		x1, x2 = x2, x1

	if y1 > y2:
		y1, y2 = y2, y1

	if y1 == y2:

		for i in range(x1, x2+1):
			graph[y1][i] += 1

	if x1 == x2:

		for j in range(y1, y2+1):
			graph[j][x1] += 1

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
