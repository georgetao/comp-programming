"""
ID: georget2
LANG: PYTHON3
TASK: milk
"""
import heapq
import sys

with open("milk.in", "r") as fin:
    n, m = map(int, fin.readline().split())

    heap = []
    for _ in range(m):
        price, units = map(int, fin.readline().split())
        heapq.heappush(heap, (price, units))
cost = 0

if n != 0:  
    curr_price, curr_units = heapq.heappop(heap)

    while n - curr_units > 0:
        n = n - curr_units
        cost += curr_price * curr_units

        curr_price, curr_units = heapq.heappop(heap)

    cost += curr_price * n

with open("milk.out", "w") as fout:
    fout.write(str(cost) + "\n") 
