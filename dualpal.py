"""
ID: georget2
LANG: PYTHON3
TASK: dualpal
"""
def isPalindrome(s):
	if len(s) < 2:
		return True
	if s[0] != s[-1]:
		return False
	return isPalindrome(s[1:-1])


def num_in_base(num, base):
	if num < base:
		return str(num)

	prefix = num_in_base(int(num / base), base)
	if prefix[0] == "0":
		prefix = prefix[1:]

	return prefix + str(num - (int(num / base) * base))


def palindrome_in_2_bases(num):
	count = 0
	for b in range(2, 11):
		s = num_in_base(num, b)
		if isPalindrome(s):
			count += 1
			if count == 2:
				return True

	return False


with open("dualpal.in", "r") as fin:
	n, s = map(int, fin.readline().split())

i = 1
with open("dualpal.out", "w") as fout:
	while n > 0:

		while not palindrome_in_2_bases(s+i):
			i += 1

		fout.write(str(s+i) + "\n")
		n -= 1
		i += 1