from itertools import product

alph = sorted('цапля')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('а') <= 1:
        if val.count('ц') == 2:
            if 'л' not in val:
                print(pos)
                break