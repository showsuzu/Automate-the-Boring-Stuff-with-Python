#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## cmdGmailer.py - 11.10.1章 コマンドラインGメイラー
# Usage:
# python cmdGmailer.py　<ID> <PW> <宛先> <タイトル> <本文>

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# seleniumのドキュメント
#  http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp
#  https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html

import sys
import logging

logging.basicConfig(level=logging.DEBUG,
#	filename='myProgramLog.txt',
	format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# 入力チェック
if len(sys.argv) > 5:
	# コマンドラインからユーザーIDを取得する
	login_id = str(sys.argv[1])
	# コマンドラインからパスワードを取得する
	login_pw = str(sys.argv[2])
	# コマンドラインから宛先を取得する
	address = str(sys.argv[3])
	# コマンドラインからタイトルを取得する
	subject = str(sys.argv[4])
	# コマンドラインから本文を取得する
	txt = ' '.join(sys.argv[5:])
	logging.debug('address:{} , subject:{}'.format(address, subject))
	logging.debug('text:{}'.format(txt))
else:
	print('使い方')
	print('python cmdGmailer.py　<宛先> <タイトル> <本文>')

# ブラウザ起動（Chrome）
browser = webdriver.Chrome()
# Gmail起動
browser.get('https://www.google.com/gmail/')

# ログイン
id_input = browser.find_element_by_id('identifierId')
id_input.send_keys(login_id)
next = browser.find_element_by_id('identifierNext')
next.click()
# タイムアウトか、遷移を待つ
try:
	element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.name, "password")))
except TimeoutException:
    print ("タイムアウトしてしまいました。ブラウザを閉じます。もう一度実行して下さい")
    browser.quit()

password_input = browser.find_element_by_name('password')
password_input.send_keys(login_pw)
next = browser.find_element_by_id('passwordNext')
next.click()
# タイムアウトか、遷移を待つ
try:
	element = WebDriverWait(browser, 10).until(EC.title_contains("Gmail"))
except TimeoutException:
    print ("タイムアウトしてしまいました。ブラウザを閉じます。もう一度実行して下さい")
    browser.quit()

# 「作成：ボタンをタップ
divs = browser.find_elements_by_xpath("//div[@role='button']")
for d in divs:
    if d.text == '作成':
        d.click()
        break
# 5秒待つ。画面遷移ではないので、WebDriverWaitは使用しない
time.sleep(5)

# 宛先に入力値をペースト
to_textarea = browser.find_element_by_name('to')
to_textarea.send_keys(address + '\n')
# 1秒待つ
time.sleep(1)

# タイトルに入力値をペースト
subject_input = browser.find_element_by_name('subjectbox')
subject_input.send_keys(subject)
# 1秒待つ
time.sleep(1)

# 本文に入力値をペースト
message_div = browser.find_element_by_xpath("//div[@aria-label='メッセージ本文']")
message_div.send_keys(txt)
# 5秒待つ
time.sleep(5)

# 送信ボタンをタップ
divs = browser.find_elements_by_xpath("//div[@role='button']")
for d in divs:
    if d.text == '送信':
        d.click()
        break

