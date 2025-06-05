from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:25][::-1]:
    num1 = int(f'11353{x}12', 25)
    num2 = int(f'135{x}21', 25)
    num = num1 + num2
    if num % 24 == 0:
        print(num // 24)
        break