"""
ID: georget2
LANG: PYTHON3
TASK: wormhole
"""
import collections
def findNext(head, hash_map):
    min_x = float('inf')
    for x in y_to_x_hm[head[1]]:
        # print(x)
        if x < min_x and x > head[0]:
            min_x = x
    
    if min_x != float('inf'):
        return hash_map[(min_x, head[1])]
    else:
        return None 


def cycle(pairings):
    hm = {}
    for pair in pairings:
        hm[pair[0]] = pair[1]
        hm[pair[1]] = pair[0]
    # print(hm)
    
    for pair in pairings:
        for i in range(2):
            head = pair[i]

            nxt = findNext(head, hm)
            # print(head)
            # print(nxt)
            while nxt:
                if nxt == head:
                    return True
                else:
                    nxt = findNext(nxt, hm)
    return False

#returns a list of all possible pairings 
def pairings(res, curr, coords): 
    if len(coords) == 2:
        curr.append(tuple(coords))

        # print(curr)
        if cycle(curr):
            res.append(curr)
        return

    pair1 = coords[0]
    for pair2 in coords[1:]:
        tmp_coords = coords[1:].copy()
        tmp_coords.remove(pair2)

        pairings(res, curr + [(pair1, pair2)], tmp_coords)



with open("wormhole.in", "r") as fin:
    n = int(fin.readline())

    coords = []
    y_to_x_hm = {}
    for _ in range(n):
        x, y = map(int, fin.readline().split())

        coords.append((x, y))
        y_to_x_hm.setdefault(y, []).append(x)
    
    # print(y_to_x_hm)
        



# print(coords)
pairs = []
pairings(pairs, [], coords)

with open("wormhole.out", "w") as fout:
    fout.write(str(len(pairs)) + "\n")