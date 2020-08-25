from os.path import getsize

file1 = './sources/stockcode.txt'
file2 = './sources/img_sample.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print(f'File Name: {file1}\t File Size: {file_size1} B')
print(f'File Name: {file2}\t File Size: {file_size2} B')