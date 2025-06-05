from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:22]:
    num1 = int(f'18{x}89957', 22)
    num2 = int(f'80{x}33', 22)
    num3 = int(f'521{x}6', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        print(num // 21)
        break