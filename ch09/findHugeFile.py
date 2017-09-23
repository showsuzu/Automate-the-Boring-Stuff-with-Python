#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# fundHugeFile.py - フォルダ配下の指定サイズよりも大きなファイル検索して画面に表示する
# Usage:
# python fundHugeFile.py
# サイズはデフォルト、100MB
import os

def find_huge_file(folder, thresh_size=1024*1024*100):
	# ファイルのリストを取得
	found_flag = 0
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			# ファイルのサイズを取得
			file_path = os.path.join(foldername, filename)
			size = os.path.getsize(file_path)

			# 判定値以上のサイズなら画面に表示
			if size > thresh_size:
				if found_flag == 0:
					print(thresh_size, 'byte over file is :')
					found_flag = 1
				print(' ', file_path, '(', str(size), 'bytes )')

	if found_flag == 0:
		print(thresh_size, 'byte over file was NOT found')


# テスト用ドライバ（メイン処理）
cur_folder = os.getcwd()
find_huge_file(cur_folder, 9000)

