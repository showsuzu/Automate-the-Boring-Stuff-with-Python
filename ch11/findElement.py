#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## findElement.py - 11.7.2章 ページの要素を見つける
# Usage:
# python findElement.py

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')

try:
	elem = browser.find_element_by_class_name('bookcover')
	print('そのクラスを持つ要素<{}>を見つけた！'.format(elem.tag_name))
except:
	print('そのクラス名を持つ要素は見つからなかった。')

# 内容が、「Read It Online」<a>タグを探し、クリックする
link_elem = browser.find_element_by_link_text('Read It Online')
link_elem.click()

