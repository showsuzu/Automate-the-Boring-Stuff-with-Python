def display_inventory(inventory):
	print('持ち主リスト：')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("アイテム総数：" + str(item_total))

stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
display_inventory(stuff)


