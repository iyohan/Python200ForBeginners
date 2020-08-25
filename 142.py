f = open('./sources/stockcode.txt', 'r')
h = open('./sources/stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()