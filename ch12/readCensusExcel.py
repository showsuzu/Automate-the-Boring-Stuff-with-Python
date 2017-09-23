#Windows
# #! python3
#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## readCensusExcel.py - 12.4 群ごとに人口と人口調査標準地域の数を集計する
# Usage:
# python readCensusExcel.py

import openpyxl, pprint
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

# county_dataに群の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
	# スプレッドシートの1行に、一つの人口調査標準地域のデータがある
	state = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# この州のキーが確実に存在するようにする（setdefault()を使って存在しないときだけ辞書を設定する）
	county_data.setdefault(state,{})
	# この州のこの群のキーが確実に存在するようにする
	county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

	# 各行が人口調査標準地域を表すので、数を一つ増やす
	county_data[state][county]['tracts'] += 1
	# この人口調査標準地域の人口だけ郡の人口を増やす
	county_data[state][county]['pop'] += int(pop)

# 新しいテキストファイルを開き、county_dataの内容を書き込む
print('結果を書き込み中...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('完了')

