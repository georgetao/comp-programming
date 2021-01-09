"""
ID: georget2
LANG: PYTHON3
TASK: transform
"""
import sys
with open("transform.in", "r") as fin:
	n = int(fin.readline())

	prev_board = []
	for _ in range(n):
		prev_board.append(fin.readline().replace("\n", ""))

	new_board = []
	for _ in range(n):
		new_board.append(fin.readline().replace("\n", ""))

#invalid trans
transform = [7]

#no change
if new_board == prev_board:
	transform.append(6)

#reflection
reflection = [""] * n
for ri in range(n):
	reflection[ri] = prev_board[ri][::-1]
if reflection == new_board:
	transform.append(4)

#rotations
for j in range(2):
	if j == 0:
		pre_rotation = prev_board.copy()
	else:
		pre_rotation = reflection
	post_rotation = [""] * n
	for i in range(1, 4):
		for ri in range(n):
			s = ""
			for ci in range(n-1, -1, -1):
				s += pre_rotation[ci][ri]
			post_rotation[ri] = s

		if post_rotation == new_board:
			if j == 0:
				transform.append(i)
			else:
				transform.append(5)
			break
			
		pre_rotation = post_rotation.copy()

res = str(min(transform))
sys.stderr.write(str(transform))

with open("transform.out", "w") as fout:
	fout.write(res + "\n")

