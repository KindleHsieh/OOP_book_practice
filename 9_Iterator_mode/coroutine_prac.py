# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/21
def tally():
    score = 0
    while True:
        increase = yield score
        score += increase


# Create teams.
white_sox = tally()
blue_jay = tally()

# initial game.
next(white_sox)
next(blue_jay)

# Add score.
white_sox.send(1)
blue_jay.send(3)


max_point_team = tally()
next(max_point_team)
for i in white_sox, blue_jay:
    if i.send(0) > max_point_team.send(0):
        max_point_team = i
print(max_point_team.__name__, max_point_team.send(0))

'''
coroutine.(協程)
建立後，要利用next()做初始化，第一次推動他。
之後只能使用send(val)將參數傳進去。

協程無法單獨取得函式內的參數，也無法print結果(例如這邊的score)。
如果有顯示接收他的結果，就要使用send()才能讓yield回傳。
'''

##################
#    logging.    #
##################
import re

# search all rows and pass the row related with regex.

# Interactive with first def and suggest the right regex.

