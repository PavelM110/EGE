from itertools import permutations

matrix = '67 567 456 35 234 123 12'.split()
graph = 'аб бг ге ез зд дв ва бв гд'.split()

print(*range(1, 8))

for p in permutations('абвгдез'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)