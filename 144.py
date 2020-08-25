with open('./sources/stockcode.txt', 'r') as f:
    for line_num, line in enumerate(f.readlines()):
        print(f'{line_num+1} {line}', end='')