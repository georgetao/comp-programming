"""
ID: georget2
LANG: PYTHON3
TASK: namenum
"""
import sys
def getNum(letter):
	letters = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], 
	["J", "K", "L"], ["M", "N", "O"], ["P", "R", "S"],
	["T", "U", "V"], ["W", "X", "Y"]]
	for i in range(2, 10):
		if letter in letters[i-2]:
			return i

with open("dict.txt", "r") as din:
	valid_names = din.readlines()

hm = {}

for name in valid_names:
	serial = ""
	name = name.strip("\n")
	for c in name:
		serial += str(getNum(c))

	if serial not in hm:
		hm[serial] = [name]
	else:
		hm[serial].append(name)

with open("namenum.in", "r") as fin:
	serial = fin.readline().replace("\n", "")


with open("namenum.out", "w") as fout:
	if serial not in hm:
		fout.write("NONE" + "\n")
	else:
		for name in hm[serial]:
			fout.write(name + "\n")


