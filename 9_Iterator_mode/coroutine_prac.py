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
#  log Analyze.  #
##################
import re


# search all rows and pass the row related with regex.
def match_regex(filename, regex):
    with open(filename) as file:
        lines = file.readlines()
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]


# Interactive with first def and suggest the right regex.
def get_serials(filename):
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'
    matcher = match_regex(filename, ERROR_RE)
    device = next(matcher)
    while True:
        print('-'*36)
        bus = matcher.send(
            f'(sd \S+) {re.escape(device)}'
        )
        print(f'bus: {bus}')
        serial = matcher.send(
            f'{bus} \(SERIAL=([^)]*)\)'
        )
        print(f'serial: {serial}')
        yield serial
        device = matcher.send(ERROR_RE)


for serial_number in get_serials('/Users/kindlemac/PycharmProjects/OOP_book_practice/9_Iterator_mode/EXAMPLE_LOG.log'):
    print(serial_number)
