#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

# mapIt.py - 11.1章 コマンドラインやクリップボードに指定した住所の地図を開く

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# コマンドラインから住所を取得する
	address = ' '.join(sys.argv[1:])
else:
	# クリップボードから住所を取得する
	address = pyperclip.paste()

print(address)

webbrowser.open('https://www.google.com/maps/place/' + address)

