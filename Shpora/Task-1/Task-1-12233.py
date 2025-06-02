from itertools import permutations

matrix = '367 568 18 58 247 127 156 234'.split()
graph = 'eh hg gc cf fa ae ed db bh bg df'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)