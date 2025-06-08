with open('24-302.txt') as file:
    data = file.readline()

def f(z, o):
    pairs = {']':'[', ')':'('}
    return pairs[z] == o

ans = 0
stack = []
last_invalid = -1

for i in range(len(data)):
    if data[i] in '([': stack.append([data[i], i])
    elif data[i] in ')]':
        if stack and f(data[i], stack[-1][0]):
            stack.pop()
            if stack:
                lenght = i - stack[-1][1]
            else:
                lenght = i - last_invalid
            ans = max(ans, lenght)
        else:
            last_invalid = i
            stack.clear()
    elif not stack: # Если символ не скобка и не внутри скобок - тоже сбой
        last_invalid = i

print(ans)