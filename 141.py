count = 1
data = []
print('If you wanna save, then just press [ENTER]')
while True:
    txt = input(f'[{count}] Things to save in file: ')
    if txt == '':
        break
    data.append(txt+'\n')
    count += 1

f = open('./sources/mydata.txt', 'w')
f.writelines(data)
f.close()