#Windows
#	#! python3
#Mac
	#! /usr/bin/env python3
#Linux
#	#! /usr/bin/python3

# printTable.py - 文字列のリストについて、縦に並べ替えて、右揃えで表示する
#  1.行数と列数を把握する
#  2.各行の最大値を把握する
#  3.行列を入れ替えながら、最大文字数に応じた右揃えを行い、表示する

def print_table(data_list):
	col_widths = [0] * len(data_list)

	# 1.行数と列数を把握する
	#行数
	row = len(data_list)
	if(row <= 0):
		sys.exit()
	#列数
	col = len(data_list[0])
	print('row = ' + str(row) + ', column = ' + str(col))
	print('----------')

	# 2.各行の最大値を把握する
	#  各行の最大文字数を設定する
	for i in range(row):
		for j in range(col):
			if(col_widths[i] < len(table_data[i][j])):
				col_widths[i] = len(table_data[i][j])

	# 3.行列を入れ替えながら、最大文字数に応じた右揃えを行い、表示する
	#  列=j、行=iとしてfor文を回す
	#  内側のforループで行を変えていくことで、元の配列の行列を入れ替える
	for j in range(col):
		for i in range(row):
			#行数が最大以外なら改行しない
			if(i < row - 1):
				print(data_list[i][j].rjust(col_widths[i]+1), end='')
			else:
				print(data_list[i][j].rjust(col_widths[i]+1))


table_data = [['apple', 'oranges', 'cherries', 'bananas'],
			  ['Alice', 'Bob', 'Carol', 'David'],
			  ['jerry', 'cake', 'puding', 'candy'],
			  ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)
