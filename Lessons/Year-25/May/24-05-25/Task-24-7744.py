with open('24-303.txt') as file:
    data = file.readline()

def f(a, b):
    matches = {')' : '(', '}' : '{', ']' : '['}
    return matches[a] == b

ans = 0

stack = []
last_good = 0
for i in range(len(data)):
    if data[i] in '{[(':
        stack.append([data[i], i])
    if data[i] in ']})':
        if stack:
            if f(data[i], stack[-1][0]):
                last_good = stack[-1][1]
                stack = stack[:-1]
            else:
                ans = max(ans, i - last_good)
                last_good = i + 1
                stack = []
        else:
            last_good = i + 1

print(ans)
