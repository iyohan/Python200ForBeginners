import os
import glob

folder = r'C:\Users\iyoha\OneDrive - handong.edu\문서\GitHub\Python200ForBeginners\sources'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)  # current dir
print(file_list)