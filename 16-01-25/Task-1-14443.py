from itertools import permutations

matrix = '23567 145 146 23 127 137 156'.split()
graph = 'bc cf fg ge ea ab ad bd cd fd ed'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)