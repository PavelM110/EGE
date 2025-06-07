with open('24-303.txt') as file:
    data = file.readline()

def match(z, o):
    alph = {')':'(', '}':'{', ']':'['}
    return alph[z] == o

# data = '123{1244+12341}[12412{124}1](111(11)}(0121{12}12)'

stack = []
ans = 0
last_invalid = -1

for i in range(len(data)):
    if data[i] in '({[': stack.append((data[i], i)) # Скобка открылась - запомним
    elif data[i] in ')}]':
        if stack and match(data[i], stack[-1][0]): # Если стек не пустой и скобка подошла к последней открытой
            stack.pop() # Забыли последнюю скобку
            if stack: # Если помним, что скобка была открыта
                lenght = i - stack[-1][1] # Всё 100% хорошо от последнего открытия
            else: # Если все скобки сошлись(закрылись)
                lenght = i - last_invalid # Всё хорошо от последнего сбоя
            ans = max(ans, lenght)
        else: # Скобка не подошла или стек пустой
            last_invalid = i # Сбой
            stack.clear() # Забыть все скобки

print(ans)



ans = 0
stack = []
last_invalid = -1

for i in range(len(data)):
    if data[i] in '({[': stack.append((data[i], i))
    elif data[i] in ')}]':
        if stack and match(data[i], stack[-1][0]):
            stack.pop()
            if stack:
                lenght = i - stack[-1][1]
            else:
                lenght = i - last_invalid
            ans = max(ans, lenght)
        else:
            last_invalid = i
            stack.clear()

print(ans)















































