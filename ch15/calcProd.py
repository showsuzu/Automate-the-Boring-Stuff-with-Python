#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## calcProd.py - 15.1 エポックタイムスタンプを使用する
# Usage:
# python calcProd.py

import time
def calc_prod():
	# 1~99999の積を求める
	product = 1
	for i in range(1, 100000):
		product = product * i

	return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('計算結果は{}桁です。'.format(len(str(prod))))
print('計算時間は{}秒でした。'.format(end_time - start_time))
