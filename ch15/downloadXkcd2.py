#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## multidownloadXkcd.py - 15.12.2 XKCDコミックをダウンロードする。ただしダウンロード済みのものはダウンロードしない。
# Usage:
# python multidownloadXkcd.py

import requests
import os
import bs4
import logging
import time

logging.basicConfig(level=logging.DEBUG,
#	filename='myProgramLog.txt',
	format=' %(asctime)s - %(levelname)s - %(message)s')

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
		# ファイルが存在しない場合に限り、ダウンロードする
		comic_url = 'http:' + comic_elem[0].get('src')	# 画像のソースをダウンロード対象とする（httpはついていないので、付け足す）
		print(comic_elem)
		image_file_name = os.path.join('xkcd', os.path.basename(comic_url))
		if not os.path.exists(image_file_name):
			logging.debug('コミック画像({})のURL{}'.format(len(comic_elem), comic_elem[0].get('src')))
			# 画像をダウンロードする
			print('画像をダウンロード中 {}...'.format(comic_url))
			res = requests.get(comic_url)
			res.raise_for_status()

			# 画像を./xkcdに保存する
			image_file = open(image_file_name, 'wb')	# comic_urlの最終節は画像のファイル名
			for chunk in res.iter_content(100000):
				image_file.write(chunk)
			image_file.close()
		else:
			print('{}は既にダウンロード済みです'.format(comic_url))

	# PrevボタンのURLを取得する
	prev_link = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prev_link.get('href')

	# 20秒インターバル
#	time.sleep(20)

print('完了')


