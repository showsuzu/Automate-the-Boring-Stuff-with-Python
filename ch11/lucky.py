#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

# lucky.py - 11.5章 Google検索結果を最大5タブ分開く。検索キーワードはコメンドラインの引数
# Usage:
# python lucky.py [検索ワード]

import requests, sys, webbrowser, bs4

print('Search word : ' + ' '.join(sys.argv[1:]))
print('Googling...')	# Googleページをダウンロード中にテキストを表示
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')

# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))
print('検索結果表示数 : ', num_open)
for i in range(num_open):
	webbrowser.open('http://google.com' + link_elems[i].get('href'))

