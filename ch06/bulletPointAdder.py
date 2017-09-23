#Windows
#	#! python3
#Mac
	#! /usr/bin/env python3
#Linux
#	#! /usr/bin/python3

# bulletPointAdder.py - クリップボードのテキストの各行に点を打ってWikipediaの箇条書きにする

import pyperclip

# 1.クリップボードからテキストを取得する
text = pyperclip.paste()

# 2.テキストを処理する
#  行を分割して、'*'を追加する
lines = text.split('\n')
for i in range(len(lines)):		# "lines"リストの各要素をループする
	lines[i] = '* ' + lines[i]	# "lines"の各要素に、"* "を追加する
text = '\n'.join(lines)			# "lines"の各要素を、"\n"で全てつなげる

# 3.新しいテキストをクリップボードにコピーする
pyperclip.copy(text)

