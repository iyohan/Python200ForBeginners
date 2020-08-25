txt = input('Things to save: ')
f = open('./sources/mydata.txt', 'w')
f.write(txt)
f.close()