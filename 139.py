f = open('./sources/stockcode.txt', 'r')  # file object
lines = f.readlines()  # return a list
for line_num, line in enumerate(lines):
    print(f'{line_num} {line}', end='')
f.close()