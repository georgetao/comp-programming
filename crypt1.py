"""
ID: georget2
LANG: PYTHON3
TASK: crypt1
"""

def generate_3_dig_num(digits) -> list:
    res = []
    for d0 in digits:
        for d1 in digits:
            for d2 in digits:
                res.append(int(str(d0) + str(d1) + str(d2)))
    return res
        

with open("crypt1.in", "r") as fin:
    n = int(fin.readline())

    digits = list(map(int, fin.readline().split()))

res = 0
    
hash_1dig = set()
hash_3dig = set()

for d in digits:
    hash_1dig.add(str(d))

_3_dig_num_list = generate_3_dig_num(digits)
for _3_dig_num in _3_dig_num_list:
    hash_3dig.add(str(_3_dig_num))

for _3_dig_num in _3_dig_num_list: #900
    possible_pps = []
    for d in digits:
        part_prod = _3_dig_num * d
        if str(part_prod) in hash_3dig:
            possible_pps.append(part_prod)
    for pp0 in possible_pps:
        for pp1 in possible_pps:
            _sum = str(pp0 + (pp1 * 10))
            if _sum[0] in hash_1dig and _sum[1:] in hash_3dig:
                # print(_sum)
                res += 1
            

with open("crypt1.out", "w") as fout:
    fout.write(str(res) + "\n")
