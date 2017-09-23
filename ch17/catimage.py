#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## catimage.py - 17.2.1 からの記事の内容（猫の画像の操作を行う）
# Usage:
# python catimage.py

from PIL import Image

cat_im = Image.open('zophie.png')			# 画像をロード
cat_copy_im = cat_im.copy()					# ロードした画像をコピー

face_im = cat_im.crop((335, 345, 565, 560))	# 画像を切り出し
cat_copy_im.paste(face_im, (0, 0))			# コピーした画像を貼り付け
cat_copy_im.paste(face_im, (400, 500))
cat_copy_im.save('pasted.png')

cat_copy_two = cat_im.copy()
for left in range(0, cat_im_width, face_im_width):
	for top in range(0, cat_im_height, face_im_height):
		# print(left, top)
		cat_copy_two.paste(face_im, (left, top))

cat_copy_two.save('tiled.png')

width, height = cat_im.size	# サイズを取得
quartersized_im = cat_im.resize((int(width / 2), int(height / 2)))	# リサイズ
quartersized_im.save('quartersized.png')

thumb_im = cat_im.copy()
thumb_im.thumbnail((100, 100))	# サムネイルを100x100Pixサイズで作成する
thumb_im.save('thumbnail.jpg')

cat_im.rotate(90).save('rotate90.png')		# rotateは元の画像を変更しないので、コピーしなくてもそのまま使用できる
cat_im.rotate(180).save('rotate180.png')
cat_im.rotate(270).save('rotate270.png')

cat_im.rotate(6).save('rotated6.png')
cat_im.rotate(6, expand=True).save('rotated6_expanded.png')	# 回転後の画像を回転後のサイズに拡大する

cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')	# 左右反転する
cat_im.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')	# 上下反転する

