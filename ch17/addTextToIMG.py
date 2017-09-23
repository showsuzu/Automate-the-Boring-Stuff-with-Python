#Mac
#! /usr/local/var/lib/pyenv/versions/anaconda3-2.0.1/python3.4
#Linux
# #! /usr/bin/python3

## addTextToIMG.py - 17.4.2 テキストを描画する
# Usage:
# python addTextToIMG.py

from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

#jfont = ImageFont.truetype('ヒラギノ明朝 ProN W3.ttc', 24, index = 1)	# MS P明朝
#draw.text((20, 20), 'こんにちは', fill = 'black', font=jfont)

# MAC OS Xの場合のrローカルフォント /Library/Fonts/
jfont = ImageFont.truetype('ヒラギノ丸ゴ ProN W4.ttc', 24, index = 0)
draw.text((20, 50), 'こんにちは', fill = 'black', font=jfont)

# MAC OS Xの場合のシステムフォント /System/Library/Fonts/
jfont = ImageFont.truetype('ヒラギノ明朝 ProN W3.ttc', 24, index = 0)
draw.text((20, 80), 'こんにちは', fill = 'black', font=jfont)

im.save('jtext.png')

