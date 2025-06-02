from itertools import permutations

matrix = '68 47 45 237 368 15 248 157'.split()
graph = 'ce eg gf fa ac cd dh he ab bf'.split()

print(*range(1, 9))

for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)