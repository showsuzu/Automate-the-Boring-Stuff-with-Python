#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# boxPrint.py - 10.1章(例外の起こし方(raise)と、try exceptの使い方)

import traceback
import datetime

def box_print(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('symbolは1文字の文字列でなければならない。')
	if width <= 2:
		raise Exception('widthは2より大きくなければならない。')
	if height <= 2:
		raise Exception('heightは2より大きくなければならない。')

	# symbolで四角を書く
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

# デバッグ用
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
	try:
		box_print(sym, w, h)
	except Exception as err:
		print('例外が起こりました：' + str(err))
		# 例外発生時のトレースバック情報をファイルに保存する
		now = datetime.datetime.now()
		filename = "errorInfo_{0:%Y%m%d-%H%M%S%f}.txt".format(now)
		error_file = open(filename, 'w')
		error_file.write(traceback.format_exc())
		error_file.close()
		print('トレースバック情報を' + filename + 'に書きました。')

