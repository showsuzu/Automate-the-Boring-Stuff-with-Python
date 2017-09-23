#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# findReg.py - 指定の正規表現にマッチするテキストファイルの行を表示する
# Usage:
# python findReg.py <正規表現>

import os, sys, re

if len(sys.argv) != 2:
	print('使い方: python findReg.py <正規表現>')
	sys.exit()

#print(sys.argv[1])
pattern = re.compile(sys.argv[1])

for filename in os.listdir('./'):
    if not filename.lower().endswith('.txt'):	# テキストファイルじゃなければ、ループに戻る
        continue

#    print(filename)
    txt_file = open(filename, 'r')
#    file_data = txt_file.read()
#    print(file_data)
    for line in txt_file:						# 1行読む　TODO　何故か読めない！
        much = pattern.search(line)
#        print(line)
        if much:
            print(filename, ':',  line, end='')

    txt_file.close()
