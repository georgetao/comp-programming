"""
ID: georget2
LANG: PYTHON3
TASK: milk2
"""

import sys
with open("milk2.in", "r") as fin:
	n = int(fin.readline())
	start_end_times = []
	for _ in range(n):
		x, y = map(int, fin.readline().split())
		start_end_times.append((x, y))

start_end_times.sort(key = lambda x: x[0])

longest_milk = 0
longest_idle = 0
curr_start = start_end_times[0][0]
curr_end = start_end_times[0][1]
for start, end in start_end_times:
	if start > curr_end:
		longest_idle = max(longest_idle, start - curr_end)
		curr_start = start
		curr_end = end

	else:
		if end > curr_end:
			curr_end = end

	longest_milk = max(longest_milk, curr_end - curr_start)

with open("milk2.out", "w") as fout:
	fout.write(str(longest_milk) + " " + str(longest_idle) + "\n")
