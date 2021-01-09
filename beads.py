"""
ID: georget2
LANG: PYTHON3
TASK: beads
"""
import sys
with open("beads.in", "r") as fin:
	n = int(fin.readline())
	beads = fin.readline().replace("\n", "")

def longest_beads(n, beads):
	curr_char = ""
	prev = 0
	curr = 0
	longest = 0
	tail_whites = 0
	newStreak = False

	for _ in range(2):
		for c in beads:
			if c == curr_char:
				curr += 1
				tail_whites = 0
			elif c == "w":
				curr += 1
				tail_whites += 1
			else:
				prev = curr
				curr_char = c
				curr = 1
				newStreak = True

			if prev + curr > longest:
				longest = prev + curr 

			if newStreak:
				curr += tail_whites
				prev -= tail_whites
				tail_whites = 0
				newStreak = False

			if longest >= n:
				return longest

	return longest

longest = longest_beads(n, beads)

with open("beads.out", "w") as fout:
	fout.write(str(longest) + "\n")
