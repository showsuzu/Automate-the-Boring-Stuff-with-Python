#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## countdown.py - 15.9 シンプルなカウントダウンスクリプト
# Usage:
# python countdown.py

import time, subprocess

time_left = 60		# カウントダウンタイムは固定で60Sec
print('timer start')
while time_left > 0:
	print(time_left, end='')
	time.sleep(1)
	time_left = time_left - 1

print('timer end')
# カウントダウン後に音声ファイルを再生する
subprocess.Popen(['open', 'alarm.wav'])

