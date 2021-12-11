#! /usr/bin/env python3

import sys

SIZE = 5
MARK = -1

def read_board():
	b = []
	for _ in range(SIZE):
		b.append(list(map(int, sys.stdin.readline().strip().split())))

	return b

def mark_board(b, n):
	for i in range(SIZE):
		for j in range(SIZE):
			if b[i][j] == n:
				b[i][j] = MARK

def check_board(b):

	# check rows
	for i in range(SIZE):
		win = True
		for j in range(SIZE):
			if b[i][j] != MARK:
				win = False
		if win:
			return True

	# check col
	for i in range(SIZE):
		win = True
		for j in range(SIZE):
			if b[j][i] != MARK:
				win = False
		if win:
			return True

	return False

def calc_board(b):
	score = 0

	for i in range(SIZE):
		for j in range(SIZE):
			if b[i][j] != MARK:
				score += b[i][j]

	return score


def print_board(b):
	for row in b:
		print(row)

def main():

	numbers = list(map(int, sys.stdin.readline().strip().split(',')))
	boards = []

	while line := sys.stdin.readline():
		boards.append(read_board())
		
	haveWinner = False
	WonBoards = [0 for _ in range(len(boards))]

	while numbers:
		num = numbers.pop(0)

		for index, board in enumerate(boards):
			if WonBoards[index] == 0:
				mark_board(board, num)
				haveWinner = check_board(board)
				if haveWinner:
					if WonBoards[index] == 0:
						lastBoard = board.copy()
						lastWinNum = num
					WonBoards[index] = 1

	print_board(lastBoard)
	score = calc_board(lastBoard)
	print(lastWinNum, score, score * lastWinNum) 
		

	


if __name__ == "__main__":
	main()
