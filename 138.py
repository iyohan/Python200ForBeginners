f = open('./sources/stockcode.txt', 'r')  # file object
line_num = 1
line = f.readline()  # return a string
while line:  # when line is '' (empty string), loop terminates
    print('{} {}'.format(line_num, line), end='')
    line = f.readline()
    line_num += 1
f.close()