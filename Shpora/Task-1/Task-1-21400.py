from itertools import permutations

matrix = '457 567 45 136 123 247 126'.split()
graph = 'fa ab bg ge ef fd da dc ec cb'.split()

print(*range(1, 8))

for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in matrix[p.index(y)] for x, y in graph):
        print(*p)