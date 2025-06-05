from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:19][::-1]:
    num1 = int(f'98{x}79641', 19)
    num2 = int(f'36{x}14', 19)
    num3 = int(f'73{x}4', 19)
    num = num1 + num2 + num3
    if num % 18 == 0:
        print(num // 18)
        break