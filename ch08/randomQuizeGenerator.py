#Windows
# #! python3
#Mac
  #! /usr/bin/env python3
#Linux
# #! /usr/bin/python3

# randomQuizeGenerator.py - ランダムに問題と答えを並べ問題集と解答集を作る

import random

# 問題のデータ。キーが都道府県で、値が県庁所在地
capitals = {'北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市',
  '宮城県': '仙台市', '秋田県': '秋田市', '山形県': '山形市', '福島県': '福島市',
  '茨城県': '水戸市', '栃木県': '宇都宮市', '群馬県': '前橋市',
  '埼玉県': 'さいたま市', '千葉県': '千葉市', '東京都': '東京',
  '神奈川県': '横浜市', '新潟県': '新潟市', '富山県': '富山市', '石川県': '金沢市',
  '福井県': '福井市', '山梨県': '甲府市', '長野県': '長野市', '岐阜県': '岐阜市',
  '静岡県': '静岡市', '愛知県': '名古屋市', '三重県': '津市', '滋賀県': '大津市',
  '京都府': '京都市', '大阪府': '大阪市', '兵庫県': '神戸市', '奈良県': '奈良市',
  '和歌山県': '和歌山市', '鳥取県': '鳥取市', '島根県': '松江市',
  '岡山県': '岡山市', '広島県': '広島市', '山口県': '山口市', '徳島県': '徳島市',
  '香川県': '高松市', '愛媛県': '松山市', '高知県': '高知市', '福岡県': '福岡市',
  '佐賀県': '佐賀市', '長崎県': '長崎市', '熊本県': '熊本市', '大分県': '大分市',
  '宮崎県': '宮崎市', '鹿児島県': '鹿児島市', '沖縄県': '那覇市'}

# 35個の問題集を作成する
for quiz_num in range(35):
  # 問題集と解凍集のファイルを作成する
  quiz_file = open('capitalsquiz{}.txt'.format(quiz_num + 1), 'w')
  answer_key_file = open('capitalsquiz_answers{}.txt'.format(quiz_num + 1), 'w')

  # 問題集のヘッダーを書く
  quiz_file.write('名前:\n\n日付:\n\n学期:\n\n')
  quiz_file.write((' ' * 20) + '都道府県庁所在地クイズ（問題番号 {})'.format(quiz_num + 1))
  quiz_file.write('\n\n')

  # 都道府県の順番をシャッフルする
  prefectuires = list(capitals.keys())
  random.shuffle(prefectuires)

  # 47都道府県をループして、それぞれ問題を作成する
  for question_num in range(len(prefectuires)):
    # 正解と解答を取得する
    correct_answer = capitals[prefectuires[question_num]]   # keyからvalueを持ってくる
    # 誤答を得る
    wrong_answers = list(capitals.values())                 # 全部の県庁所在地を取得し
    del wrong_answers[wrong_answers.index(correct_answer)]  # 正しい答えのみを削除
    wrong_answers = random.sample(wrong_answers, 3)         # ランダムに３つを抽出
    # 4つの選択肢をまとめる
    answer_options = wrong_answers + [correct_answer]       # 正解と３つの誤答をまとめ
    random.shuffle(answer_options)                          # 4つの選択肢をシャッフルする

    # 問題文と回答選択肢を問題ファイルに書く
    quiz_file.write('{}. {}の都道府県庁所在地は？\n'.format(question_num + 1, prefectuires[question_num]))
    for i in range(4):
      quiz_file.write(' {}. {}\n'.format('ABCD'[i], answer_options[i]))

    quiz_file.write('\n')

    # 答えの選択肢を解凍ファイルに書く
    answer_key_file.write('{}. {}\n'.format(question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

  quiz_file.close()
  answer_key_file.close()

