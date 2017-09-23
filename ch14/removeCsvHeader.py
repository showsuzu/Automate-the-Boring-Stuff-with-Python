#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## removeCsvHeader.py - 14.2 カレントディレクトリの全CSVファイルから見出しを削除する
# Usage:
# python removeCsvHeader.py

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# カレントディレクトリの全ファイルをループする
for csv_filename in os.listdir('.'):
	if not csv_filename.endswith('.csv'):
		continue	# CSVファイルでなければスキップする

	print('見出し削除中 ' + csv_filename + '...')

	# CSVファイルを読み込む（最初の行をスキップする）
	csv_rows = []
	csv_file_obj = open(csv_filename)
	reader_obj = csv.reader(csv_file_obj)
	for row in reader_obj:		# １行ずつ読んで
		if reader_obj.line_num == 1:
			continue			# 最初の行をスキップする
		csv_rows.append(row)	# 1行を書き出す
	csv_file_obj.close()

	# CSVファイルを書き出す
	csv_file_obj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
	csv_writer = csv.writer(csv_file_obj)
	for row in csv_rows:
		csv_writer.writerow(row)
	csv_file_obj.close()

