#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

# downloadXkcd.py - 11.6章 XKCDコミックを一つずつダウンロードする
# Usage:
# python downloadXkcd.py

import requests, os, bs4
import logging

logging.basicConfig(level=logging.DEBUG,
#	filename='myProgramLog.txt',
	format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)	# ./xkcdに保存するようにフォルダを作成する

while not url.endswith('#'):		# xkcdサイトの作りとして、最初のページのPREVボタンには、＃がhrefに設定されている
	# ページをダウンロードする
	print('ページをダウンロード中{}...'.format(url))
	res = requests.get(url)			# 1ページをダウンロード
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	# コミック画像のURLを見つける
	comic_elem = soup.select('#comic img')	# xkcdサイトの作りとして、コミックは画像で、divタグのid=comicの中のimgタグに貼られている
	if comic_elem == []:
		print('コミック画像が見つかりませんでした。')
	else:
		logging.debug('コミック画像({})のURL{}'.format(len(comic_elem), comic_elem[0].get('src')))
		comic_url = 'http:' + comic_elem[0].get('src')	# 画像のソースをダウンロード対象とする（httpはついていないので、付け足す）
		# 画像をダウンロードする
		print('画像をダウンロード中 {}...'.format(comic_url))
		res = requests.get(comic_url)
		res.raise_for_status()

		# 画像を./xkcdに保存する
		image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')	# comic_urlの最終節は画像のファイル名
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

	# PrevボタンのURLを取得する
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')

print('完了')

