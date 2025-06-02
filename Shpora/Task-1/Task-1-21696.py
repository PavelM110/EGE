from itertools import permutations

matrix = '23 168 158 578 347 27 456 234'.split()
graph = 'eh hg gc cf fa ae ed db bh bg df'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)