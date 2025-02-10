from itertools import permutations

matrix = '56 378 26 68 17 134 258 247'.split()
graph = 'CF FD DH HG GA AC AB BC BE ED'.split()

print(*range(1, 9))

for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)