#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

# downloadAndSave.py - 11.2.3章 ダウンロードしたファイルを保存する

import requests

# Automate the boring stuffの公式サイトから、ロミオとジュリエットの記事をダウンロードする
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
	res.raise_for_status()									# ダウンロードできない場合は、Exceptionが発生する
	play_file = open('RomeoAndJuliet.txt', 'wb')			# ダウンロードしたオブジェクトを保存するファイル
	for chunk in res.iter_content(100000):					# 100kサイズのchunk毎に回す。
		play_file.write(chunk)
except Exception as exc:
	print('ダウンロードに問題がありました: {}'.format(exc))

play_file.close()

