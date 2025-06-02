from itertools import permutations

matrix = '38 58 146 36 27 347 568 127'.split()
graph = 'de ea ah hc cf fg gb bd eb hg'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)