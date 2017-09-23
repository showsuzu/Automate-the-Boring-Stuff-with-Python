#Windows
#	#! python3
#Mac
	#! /usr/bin/env python3
#Linux
#	#! /usr/bin/python3

# pwCheck.py - パスワードの強度をチェックする。
#              8文字以上、大文字と小文字、数値を含む
#              戻り値：TRUE ：強いPW
#                     FALSE：弱いPW

import sys, re

# 入力チェック
if len(sys.argv) < 2:
	print('使い方: python pwCheck.py [パスワード]')
	print('パスワードの強い、弱いを返します')
	sys.exit()

# パスワードを取得
pw = sys.argv[1] #最初のコマンドライン引数がパスワード

# チェックする正規表現
#  ^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z\-_]{8,}$
#  NGの内容を案内したいので、それぞれを分解して正規表現を記載する
#  他に良い書き方があるはず

#  文字数が8文字以上あるか？
pwlen_regex = re.compile(r'[\d\w]{8,}')

#  小文字が含まれているか？
pwlowcase_regex = re.compile(r'[a-z]+')

#  大文字が含まれているか？
pwbigcase_regex = re.compile(r'[A-Z]+')

#  数字が含まれているか？
pwdig_regex = re.compile(r'[0-9]+')

#  禁則文字は含まれていないか？
pwng_regex = re.compile(r'[ ¥#$%&\'"!?+-/*.]')

#  開始文字は英数字か？
pwstword_regex = re.compile(r'^[0-9a-zA-Z]')

# NGカウンタ
count = 0

if pwlen_regex.search(pw) == None:
	print('パスワードは8文字以上必要です')
	count += 1

if pwlowcase_regex.search(pw) == None:
	print('パスワードは小文字を1文字以上含んで下さい')
	count += 1

if pwbigcase_regex.search(pw) == None:
	print('パスワードは大文字を1文字以上含んで下さい')
	count += 1

if pwdig_regex.search(pw) == None:
	print('パスワードは数字を1文字以上含んで下さい')
	count += 1

if pwstword_regex.search(pw) == None:
	print('パスワードの先頭文字は英数文字のいずれかにして下さい')
	count += 1

if pwng_regex.search(pw) != None:
	print('パスワードには使用できない文字が入っています')
	count += 1

if count == 0:
	print("OKです")
#	return True

#return False

