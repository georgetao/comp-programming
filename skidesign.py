"""
ID: georget2
LANG: PYTHON3
TASK: skidesign
"""
import collections

def cost(arr):
    cost = 0
    for num in arr:
        cost += pow(num, 2)
    return cost

with open("skidesign.in", "r") as fin:
    n = int(fin.readline())

    hill_heights = []
    for _ in range(n):
        hill_heights.append(int(fin.readline()))
    
lowest_cost = float('inf')
for min_h in range(0, 84):
    change = []
    for h in hill_heights:
        if h < min_h:
            change.append(min_h - h)
        if h > min_h + 17:
            change.append(min_h + 17 - h)
    
    curr_cost = cost(change)
    if curr_cost < lowest_cost:
        lowest_cost = curr_cost 



with open("skidesign.out", "w") as fout:
    fout.write(str(lowest_cost) + "\n")