#! /usr/bin/env python3
import re
import sys
import collections

START = 'start'
END = 'end'

def build_graph():
	graph = collections.defaultdict(list)

	while line := sys.stdin.readline().strip():

		s, d = line.split('-')
		graph[s].append(d)
		graph[d].append(s)

	return graph


def find_paths(graph, node, curr_path, visited, paths):
	if len(curr_path) > 1 and node == END:

		paths.append(curr_path.copy())

	#print(curr_path, visited)

	for n in graph[node]:

		if n in visited:
			continue

		if not n.isupper():
			visited.append(n)

		curr_path.append(n)

		find_paths(graph, n, curr_path, visited, paths)
		
		if n in visited:
			visited.remove(n)

		curr_path.remove(n)


	return
	
	

def main():
	graph = build_graph()


	visited = [START]
	path = [START]
	paths = []
	
	find_paths(graph, START, path, visited, paths)

	print(len(paths))
	
if __name__ == "__main__":
	main()
