#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# walk_dir.py - ディレクトリツリーを渡り歩く(このスクリプトを実行しているカレントフォルダ限定)
# Usage:
# python walk_dir.py

import os, shutil

cur_dir = os.getcwd()
print(cur_dir)

for foldername, subfolders, filenames in os.walk(cur_dir):
	print('The current folder is ' + foldername)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + foldername + ': ' + subfolder)

	for filename in filenames:
		print('FILE INSIDE ' + foldername + ': ' + filename)

	print('')


