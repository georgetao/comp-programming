"""
ID: georget2
LANG: PYTHON3
TASK: combo
"""
def generate_codes(code, n):
    res = [[]]
    for num in code:
        next_res = []
        for x in res:
            # print(x)
            for i in range(-2, 3):
                next_res.append(x + [((num + i - 1) % n) + 1])
                
        # print(next_res)
        res = next_res.copy()
    
    return res

with open("combo.in", "r") as fin:
    n = int(fin.readline())
    f_code = tuple(map(int, fin.readline().split()))
    m_code = tuple(map(int, fin.readline().split()))

working_codes = set()

for code in generate_codes(f_code, n) + generate_codes(m_code, n):
    # print(code)
    working_codes.add(tuple(code))

# print(working_codes)
with open("combo.out", "w") as fout:
    fout.write(str(len(working_codes)) + "\n")