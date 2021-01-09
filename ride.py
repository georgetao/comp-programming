"""
ID: georget2
LANG: PYTHON3
TASK: ride
"""
with open("ride.in", "r") as fin:
	comet = fin.readline()
	group = fin.readline()
fout = open("ride.out", "w")



comet_val = 1
for c in comet:
	comet_val *= ord(c) - ord('A') + 1

group_val = 1
for c in group:
	group_val *= ord(c) - ord('A') + 1

with open("ride.out", "w") as fin:
	if group_val % 47 == comet_val % 47:
		fout.write("GO\n")
	else:
		fout.write("STAY\n")