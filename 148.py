from os import rename

target_file = './sources/stockcode.txt'
newname = input('new name for file {}: '.format(target_file))
rename(target_file, newname)  # incl. path. without it, current dir.