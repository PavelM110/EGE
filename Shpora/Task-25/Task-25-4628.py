from fnmatch import fnmatch

for i in range(124065 - 124065 % 161, 10**8, 161):
    if fnmatch(f'{i}', '12*4?65'):
        print(i, i // 161)