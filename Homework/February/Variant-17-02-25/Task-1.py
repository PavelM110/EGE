from itertools import permutations

matrix = '235 13 1245678 36 13 347 368 37'.split()
graph = 'аб бг ге ез зж жд дг гв ва аг гз гж'.split()

print(*range(1, 9))

for p in permutations('абвгдежз'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)