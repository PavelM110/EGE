from fnmatch import fnmatch

for i in range(120076 - 120076 % 1923, 10**8, 1923):
    if fnmatch(f'{i}', '1*2??76'): print(i, i // 1923)