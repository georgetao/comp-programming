"""
ID: georget2
LANG: PYTHON3
TASK: gift1
"""

import sys

fin = open("gift1.in", "r")
np = int(fin.readline())

names_list = []
names_dict = {}
for _ in range(np):
	name = fin.readline().replace("\n", "")
	names_dict[name] = 0
	names_list.append(name)

for _ in range(np):
	giver = fin.readline().replace("\n", "")
	amt, ppl = map(int, fin.readline().split())
	if ppl == 0:
		continue

	split_amt = int(amt / ppl)
	names_dict[giver] -= (split_amt * ppl)

	for _ in range(ppl):
		taker = fin.readline().replace("\n", "")
		names_dict[taker] += split_amt

fout = open("gift1.out", "w")
for name in names_list:
	fout.write(name + " " + str(names_dict[name]) + "\n")
