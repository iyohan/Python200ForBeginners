from os import remove

target_file = './sources/stockcode_copy.txt'
k = input(f'Do you want to remove file {target_file} (y/n): ')
if k == 'y':
    remove(target_file)
    print(f'{target_file} is successfully removed.')