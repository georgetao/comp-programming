"""
ID: georget2
LANG: PYTHON3
TASK: palsquare
"""
def is_palindrome(s):
	if len(s) <= 1:
		return True
	if s[-1] != s[0]:
		return False
	return is_palindrome(s[1:-1])

def in_base_b(num, b):

	if num < b:
		if num > 9:
			return chr(ord("A") + num - 10)
		if num == 0:
			return 0
		else:
			return str(num)

	prefix = in_base_b(int(num / b), b)

	s = num - (int(num / b) * b)
	if s > 9:
		s = chr(ord("A") + s - 10)

	if prefix[0] == "0":
		prefix.pop(0)
	return prefix + str(s)

with open("palsquare.in", "r") as fin:
	b = int(fin.readline())

i = 0

fout = open("palsquare.out", "w")

for j in range(1, 301):
	squared = in_base_b(j * j, b)

	if is_palindrome(squared):
		num = in_base_b(j, b)
		fout.write(num + " " + squared + "\n")