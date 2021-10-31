# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/31

# 目前為止都沒有設置參數，如同unitest飯粒的StatsList.
# pytest 有兩種設置方式：
# 第一種是利用func名稱。 def pytest_funcarg__<arg name>(request):
# 此種方式是在單一module上使用(通用)。
# request 提供方法與屬性來修改fumcarg的行為。
# 第二種是建立conftest.py，這種就類似『全域』，可以再多module內傳送。。
from stats import StatsList


def pytest_funcarg__valid_stats(request):
    return StatsList([1, 2, 2, 3, 3, 4])


def test_mean(valid_stats):
    assert valid_stats.mean() == 2.5


def test_median(valid_stats):
    assert valid_stats.median() == 2.5
    valid_stats.append(4)
    assert valid_stats.median() == 3


def test_mode(valid_stats):
    assert valid_stats.mode() == [2, 3]
    valid_stats.remove(2)
    assert valid_stats.mode() == [3]


