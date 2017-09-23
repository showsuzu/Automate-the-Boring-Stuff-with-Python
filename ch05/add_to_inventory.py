def display_inventory(inventory):
	print('持ち主リスト：')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("アイテム総数：" + str(item_total))

def add_to_inventory(inventory, added_items):
	#dragon_lootのアイテムを取得していく
	for k in added_items:
		#既にあればそのままの値。なければ初期値のゼロをセットする
		inventory.setdefault(k, 0)
		inventory[k] += 1
	#inventoryを返す
	return inventory


inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
#invは参照渡しになるので戻り値を保存せずとも、元のデータが変更される
#inv = add_to_inventory(inv, dragon_loot)
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
