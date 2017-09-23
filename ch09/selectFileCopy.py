#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# selectFileCopy.py - 指定した拡張子のファイルをみつけて、新しいフォルダ(New)にコピーする
# Usage:
# python selectFileCopy.py

import os, shutil

def file_copy(extension, folder):
	# フォルダのツリーを渡り歩いて引数の拡張子を持つファイルを検索する
	# 検索するフォルダはカレントフォルダとその配下
	# os.walkを使えば、そのフォルダのファイルリストが入手できる（以下では、filenames）
	mkdir_flag = 0
	cur_folder = os.getcwd()
	extension = extension.lower()
	new_folder = folder + '_'
#	print(new_folder)
	for foldername, subfolders, filenames in os.walk(cur_folder):
		if os.path.basename(foldername).startswith(new_folder):
			continue											# 追加したフォルダならその中を検索しない

		print('Searching files in {}...'.format(foldername))
		# 現在のフォルダの中の全ファイルの拡張子を検査する
		for filename in filenames:
			if not filename.lower().endswith('.' + extension):
				continue		# 対象の拡張子でなければ、コピーしない

			# コピーすべきファイルが見つかったら、コピー先のフォルダを作成する
			if mkdir_flag == 0:
				number = 1
				while True:
					new_foldername = new_folder + str(number)
					if not os.path.exists(new_foldername):
						break
					number = number + 1
				os.mkdir(new_foldername)			# 現在のフォルダの中に新しいフォルダを作成する
				mkdir_flag = 1

			# ファイルをコピーする
			print('Copying ' + os.path.join(foldername, filename) + ' to ' + new_foldername)
			shutil.copy(os.path.join(foldername, filename), new_foldername)

	if mkdir_flag == 0:
		print('拡張子 : ' + extension + ' のファイルが見つかりませんでした')
	else:
		print('Done')


# テスト用ドライバー
#  検索拡張子はjpeg
extension = 'jpg'
folder = 'jpgs'
file_copy(extension, folder)
