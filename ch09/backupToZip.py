#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# backupToZip.py - フォルダ全体を連番付きZIPファイルにコピーする
# Usage:
# python backupToZip.py

import zipfile, os

def backup_to_zip(folder):
#	print('Input folder : ' + folder)
	# フォルダ全体をZIPファイルにバックアップする
	folder = os.path.abspath(folder)	# folderを絶対パスにする

#	print('Absolute folder path : ' + folder)
#	print('basename : ' + os.path.basename(folder))
	# 既存のファイル名からファイル名の連番を決める
	number = 1
	while True:
		zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zip_filename):
			break
		number = number + 1

	# ZIPファイルを作成する
	print('Creating {}...'.format(zip_filename))
	backup_zip = zipfile.ZipFile(zip_filename, 'w')

	# フォルダのツリーを渡り歩いてその中のファイルを圧縮する
	# os.walkを使えば、そのフォルダのファイルリストが入手できる（以下では、filenames）
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files in {}...'.format(foldername))
		# 現在のフォルダをZIPファイルに追加する
		backup_zip.write(foldername)
		# 現在のフォルダの中の全ファイルをZIPファイルに追加する
		for filename in filenames:
			new_base = os.path.basename(folder) + '_'
			if filename.startswith(new_base) and filename.endswith('.zip'):
				continue		# バックアップ用ZIPファイル（foldername_**.zip）はバックアップしない
			backup_zip.write(os.path.join(foldername, filename))
	backup_zip.close()
	print('Done')


cur_dir = os.getcwd()
backup_to_zip(cur_dir)
