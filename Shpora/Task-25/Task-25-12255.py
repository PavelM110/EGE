from fnmatch import fnmatch

for i in range(1203456009 - 1203456009 % 98591, 10**12, 98591):
    if fnmatch(f'{i}', '12?3*456??9'): print(i, i // 98591)