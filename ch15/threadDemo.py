#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## threadDemo.py - 15.6 マルチスレッドデモ
# Usage:
# python threadDemo.py

import threading
import time

print('プログラム開始')

def take_a_nap():
	time.sleep(5)	# 5秒間停止
	print('起きた！')

thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('プログラム終了')
