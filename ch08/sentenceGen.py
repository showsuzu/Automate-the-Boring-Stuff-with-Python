#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# sentenceGen.py - ADJECTIVE、NOUN、ADVERB、VERBを指定のワードに書き換える
# Usage:
# python sentenceGen.py <soucefile>

import re, sys

# 引数をチェックする
if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	print('使い方: python sentenceGen.py <soucefile>')
	sys.exit()

# ファイルを読む
src_file = open(filename, 'r', encoding='utf-8')
src_data = src_file.read()							# fileの内容
src_file.close()									# 不要なので、ファイルはクローズする

# 対象のワードが含まれているかを確認する
chg_pattern = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')

# 対象のワード分、以下を繰り返す
#   対象のワードの置き換えをユーザーに入力させる
#   入力ワードを変更する
while True:
	pu_word = chg_pattern.search(src_data)
	if not pu_word:		# マッチしたワードがなければwhileループを抜ける
		print('break infinity roop')
		break

	print('Enter an ' + pu_word.group(1).lower() + ' : ', end='')
	chg_word = input()
	if chg_word != '':
		# 一つだけ変換する。空入力のときは何もせずにループに戻る
		src_data = src_data.replace(pu_word.group(1), chg_word, 1)


# 画面に表示する
print(src_data)
# 新しい名前でファイルを保存する
filename = 'chg_' + filename
dst_file = open(filename, 'w', encoding='utf-8')
dst_file.write(src_data)
dst_file.close()

