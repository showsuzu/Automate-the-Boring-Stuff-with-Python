#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# python mcb.pyw save <keyword> - クリップボードをキーワードに紐付けて保存
# python mcb.pyw <keyword> - キーワードに紐付けて保存されたテキストをクリップボードにコピー
# python mcb.pyw list - 全キーワードをクリップボードにコピー
#
# py.exe mcb2.pyw delete <keyword> - キーワードに紐づけられたテキストを削除
# py.exe mcb2.pyw delete all - すべてのテキストを削除

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcb_shelf[sys.argv[2]] = pyperclip.paste()
	elif sys.argv[1].lower() == 'delete':
		if sys.argv[2].lower() == 'all':
			mcb_shelf.clear()			# shelveの中を全てクリアする
		else:
			del mcb_shelf[sys.argv[2]]	# 指定したキーワードのshelfを削除する
elif len(sys.argv) == 2:
	# キーワード一覧と、内容の読み込み
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcb_shelf.keys())))	# リスト全部をクリップボードにコピーする
	elif sys.argv[1] in mcb_shelf:
		pyperclip.copy(mcb_shelf[sys.argv[1]])		# キーワードがあればクリップボードにコピーする
else:
    print("""使い方：
py.exe mcb2.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
py.exe mcb2.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
py.exe mcb2.pyw list - 全キーワードをクリップボードにコピー
py.exe mcb2.pyw delete <keyword> - キーワードに紐づけられたテキストを削除
py.exe mcb2.pyw delete all - すべてのテキストを削除
""")


mcb_shelf.close()

