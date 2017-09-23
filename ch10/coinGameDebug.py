#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# coinGameDebug.py - 10.8.1章(コイン投げのデバッグ)

import random
guess = ''
while guess not in('1', '0'):
    print('コインの表裏を当てて下さい。表か裏を入力して下さい：')
    guess = str(input())
    toss = str(random.randint(0, 1)) #0=裏、1=表
    if toss == guess:
        print('あたり！')
    else:
        print('はずれ！もう一回当てて！')
        guess = str(input())
        if toss == guess:
            print('あたり！')
        else:
            print('はずれ。このゲームは苦手ですね。')


