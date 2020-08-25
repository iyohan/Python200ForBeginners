from os import rename  # study again

target_file = './sources/stockcode.txt'
newpath = './'

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath + '/' + target_file

try:
    rename(target_file, newname)
except FileNotFoundError as e:
    print(e)