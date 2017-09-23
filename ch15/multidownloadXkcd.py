#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## multidownloadXkcd.py - 15.7 XKCDコミックをマルチスレッドでダウンロードする
# Usage:
# python multidownloadXkcd.py

import requests
import os
import bs4
import threading
import logging

os.makedirs('xkcd', exist_ok=True)

logging.basicConfig(level=logging.CRITICAL,
#	filename='myProgramLog.txt',
	format=' %(asctime)s - %(levelname)s - %(message)s')

def download_xkcd(start_comic, end_comic):
	for url_number in range(start_comic, end_comic):
		# ページをダウンロードする
		print('ページをダウンロード中 http://xkcd.com/{}...'.format(url_number))
		res = requests.get('http://xkcd.com/{}'.format(url_number))			# ページをダウンロード
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

# メイン処理
# Threadオブジェクトを生成して開始する
download_threads = []		# 全Threadオブジェクトのリスト
comic_num = 100
for i in range(1, 1400, comic_num):	# 14回ループして、14個のスレッドを生成する
	download_thread = threading.Thread(target=download_xkcd, args=(i, i + comic_num))
	download_threads.append(download_thread)
	download_thread.start()

# 全てのスレッドが終了するのを待つ
for download_thread in download_threads:
	download_thread.join()

print('完了')

