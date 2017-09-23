#Windows
#	#! python3
#Mac
	#! /usr/bin/env python3
#Linux
#	#! /usr/bin/python3

# pw.py - パスワード管理プログラム（脆弱性あり）

# まずはパスワードを辞書に定義
PASSWORDS = {'email': 'F7minlBDDuvMJxESSKHFhTxFtjvB6',
			 'blog':  'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
			 'luggage': '12345'}

import sys
import pyperclip  # クリップボードにコピーするために使用する

# 入力チェック
if len(sys.argv) < 2:
	print('使い方: python pw.py [アカウント名]')
	print('パスワードをクリップボードにコピーします')
	sys.exit()

# パスワードを取得したいアカウント名の決定
account = sys.argv[1] #最初のコマンドライン引数がアカウント名

# アカウントに応じたパスワードを取得
#  辞書の中からaccountに応じたパスワードをクリップボードにコピーする
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print(account + 'のパスワードをクリップボードにコピーしました')
else:
	print(account + 'というアカウント名はありません')

