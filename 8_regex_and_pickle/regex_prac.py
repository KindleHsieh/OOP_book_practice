# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/21
import re

# print(f"{'burger':10s}{5: ^9d}${2.0000: <8.2f}${10.00000: >7.2f}")


# re.match(string), 是用來從字串中，查詢相符的部分。
# 會從[字串]的開始查詢相符。
# 解譯器會在『找到時，立即停止』。

def regex_generic(pattern, search_string):
    match = re.match(pattern, search_string)
    print('----------new_regex search----------')
    # print(match)

    if match:
        template = f"[{search_string}] matches pattern [{pattern}]"
    else:
        template = f"[{search_string}] doesn't matched pattern [{pattern}]"
    print(template)
    print('\n')


# 因為 沒有開頭是e的字串，即使剩下是對的也沒有用，因為這個字串就是錯的了。
regex_generic('ello word', 'hello word')

# 給定開頭與結尾的符號。  ＾：開頭，＄：結尾。
regex_generic('ello word', 'hello word')
regex_generic("^hello ", 'hello word')


# 句號[.]表示可以用來代表任何單一字元。 也就是不能為空，可以為空格。
regex_generic('.ello word', 'hello word')
regex_generic('hello.word', 'hello word')


# 若是要在特定的字元範圍內搜尋任一，就要使用[]建立範圍。
# [] 稱為字元集合或是字元類別。
regex_generic('hell[olpdf].word', 'hello word')


# 如果是想要建立的範圍是 “所有小寫字母”、“所有大寫字母”、“所有字母”、“所有數字”
regex_generic('hell[a-z].word', 'hello word')
regex_generic('hell[A-Z].word', 'hello word')
regex_generic('hell[a-zA-Z].word', 'hello word')
regex_generic('hell[0-9].word', 'hello word')


# 跳脫字元。
# \. \[ \] \( \).   代表著那些被拿去使用的特殊符號的顯示。
# \n (換行)  \t (tab)  \s (空白字元)  \w (字母、數字、底線)  \d (數字)。
regex_generic("\(abc\]", "(abc]")
regex_generic(" 1a", "\s\d\w")
regex_generic("\s\d\w", "\t5n")
regex_generic("\s\d\w", " 5n")


# 查詢多個字元。
# * 前個『樣式』可以重複 0或多次，也就是選擇性的，可有可無。
# + 前個『樣式』可以重複 1或多次，也就一定要有，但不限次數。
# ? 前個『樣式』可以重複 0或1次，也是選擇性的，可以有，但限定一次。
# {n,m} 前個『樣式』可以重複 n到m次，n 不可為0。
regex_generic('hel*o', 'helllllllllllllo')
regex_generic('hel*o', 'heo')
regex_generic('hel*o', 'helo')
regex_generic('he[olp]*o', 'heppppppo')
regex_generic('\d+\.\d+', '0.3333')
regex_generic('\d+\.\d+', '000.3333')
regex_generic('\d?\.\d+', '0.3333')
regex_generic('\d?\.\d+', '000.3333')
regex_generic('ca{1,3}ndy', 'candy')
regex_generic('ca{1,3}ndy', 'caaaaaaandy')
regex_generic('c(a?){1,3}ndy', 'cndy')  # 藉由?與限制次數範圍，可以規劃出限定的次數從0開頭。
regex_generic('abc{3}', 'abcc')  # 只能重複三次。


# 從正規表示式取得資訊。
# match 回答了我們，此字串與樣式是否相符。
# 但我們有時候會想知道的是，如果字串與樣式相符，相關的子字串值是什麼？
pattern = '^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$'
search_string = "some.user@example.com"
match = re.match(pattern, search_string)
if match:
    print('\n====================================\n')
    print(f"{'Which words match the groups.':-^36s}")

    for domain in (match.groups()):
        print(domain)
