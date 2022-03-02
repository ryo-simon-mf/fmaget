# -*- coding: utf-8 -*-
 
import random
from janome.tokenizer import Tokenizer
  
# Janomeを使用してテキストデータを単語に分割する
def wakati(text):
    text = text.replace('\n','') #改行を削除
    text = text.replace('\r','') #スペースを削除
    t = Tokenizer()
    result =t.tokenize(text, wakati=True)
    return result
 
#デフォルトの文の数は5
def generate_text(num_sentence=5):
    filename = "test.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)
  
    #マルコフ連鎖用のテーブルを作成
    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word
  
    #文章の自動生成
    count_kuten = 0 #句点「。」の数
    num_sentence= num_sentence
    sentence = ""
    w1, w2  = random.choice(list(markov.keys()))
    while count_kuten < num_sentence:
        tmp = random.choice(markov[(w1, w2)])
        sentence += tmp
        if(tmp=='。'):
            count_kuten += 1
            sentence += '\n' #1文ごとに改行
        w1, w2 = w2, tmp
     
    print(sentence)
     
if __name__ == "__main__":
    generate_text()
