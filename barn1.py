"""
ID: georget2
LANG: PYTHON3
TASK: barn1
"""
import heapq
with open("barn1.in", "r") as fin:
    m, s, c = map(int, fin.readline().split())

    stalls = [-1] * s
    min_i = s-1
    max_i = 0
    for _ in range(c):
        stall_num = int(fin.readline()) - 1
        stalls[stall_num] = 1

        if stall_num < min_i:
            min_i = stall_num
        if stall_num > max_i:
            max_i = stall_num

covered_stalls = max_i - min_i + 1

gaps = []

curr_gap = 0
for stall in stalls[min_i: max_i + 1]:
    if stall == 1:
        heapq.heappush(gaps, -curr_gap) 
        curr_gap = 0
    
    else:
        curr_gap += 1

while m - 1 > 0:
    try:
        covered_stalls += heapq.heappop(gaps)
        m -= 1
    except IndexError:
        break

with open("barn1.out", "w") as fout:
    fout.write(str(covered_stalls) + "\n")