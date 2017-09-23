#Windows
#	#! python3
#Mac
	#! /usr/bin/env python3
#Linux
#	#! /usr/bin/python3

# pyStrip.py - strip()の動きを正規表現で作成する

import sys, re

# 引数チェック
if len(sys.argv) < 2:
	print('使い方: python pyStrip.py [文字列,追加除去文字]')
	sys.exit()

# パスワードを取得
string = sys.argv[1] #最初のコマンドライン引数がパスワード

# 前から、スペースとタブを削除（数字、単語、空白文字以外にマッチする）正規表現
st_pu_regex = re.compile(r'^(\s)*(\S)(\d\w\s)*')

# 後から、スペースとタブを削除（数字、単語、空白文字以外にマッチする）正規表現
ed_pu_regex = re.compile(r'(\s)+$')

# 前から空白文字を省く
pu_str = st_pu_regex.sub(r'\2', string)
print(string)
print(pu_str)

# 後から空白文字を省く
pu_str = ed_pu_regex.sub(r'\1', pu_str)
print(pu_str)

# TODO 2つ目の引数があれば、引数の文字を一つずつ
if len(sys.argv) == 3:
	out_str = sys.argv[2]

