"""
ID: georget2
LANG: PYTHON3
TASK: friday
"""
fin = open("friday.in", "r")

num_years = int(fin.readline())

day = 0
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekdays = [0] * 7

for n in range(1900, 1900 + num_years):
	for month in range(12):
		_13th = 13 + day
		weekday = _13th % 7
		weekdays[weekday] += 1
		day += days_per_month[month]
		if month == 1 and ((n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)):
			curr_days += 1

res = str(weekdays[6])
for i in range(6):
	res += " " + str(weekdays[i])

fout = open("friday.out", "w")
fout.write(res + "\n")
