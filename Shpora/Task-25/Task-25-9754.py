from fnmatch import fnmatch

for i in range(30157 - 30157 % 2023, 10**8, 2023):
    if fnmatch(f'{i}', '3?1*57'): print(i, i // 2023)