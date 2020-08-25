spos = 105  # position to read file
size = 500  # read size

f = open('./sources/stockcode.txt', 'r')
h = open('./sources/stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()
