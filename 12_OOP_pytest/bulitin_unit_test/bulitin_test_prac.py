# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/28

# 為何需要測試程式？ 因為要確保我們所設計的功能能有如預期的結果。
# 並且千萬不要認為自己只是多賺寫幾行程式，一定不會影響到元程式，只能說，世事難料。
# 當程式還小得時候，會認為轉謝單元測試是在脫褲子放屁，很麻煩；但是程式成長的很快，
# 很快地就會變成大程式，或著多人協作，這樣就會凸顯出單元測試的重要性。
# 撰寫測試的四個主因：
# - 確保程式已開發者所想的方式運作。
# - 確保程式在修改後還能運作。
# - 確保開發者理解需求。
# - 確保程式已可維護的介面撰寫。
#
# 單元測試：
# 中心思想： 先寫測試，再寫程式碼。  (測試導向開發)
# 精神1： 為測試的程式都是有問題的程式。  認為只有還沒有寫出的程式不需要測試。
# 精神2： 還沒有寫出測試程式之前不要撰寫任何程式。
# 原因是，先撰寫測試可以讓我們專注於思考程式如何互動。  在我們撰寫新物件的測試的時候，就會發現設計中的異常，
# 會強迫我們思考軟體新角度。
# 每個測試應該完全獨立於其他測試。
# 撰寫好的單元測試的關鍵在於簡短、只測試一個小單元。。


# Testing.
# 當想要特定任務的單元測試時，需要建構TestCase的 sub class。
# 並讓要測試的內容使用個別的方法，這些方法要以test開頭。

import unittest
import os


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual('1', 1.0)


# 前個例子所用的assertEqual是檢查的方式，unittest有很多種方法。
# 其他的 assertRaises 則是用來確保特定函式呼叫會拋出例外。  也就是期望這樣的組合是會有某種錯誤(exception)發生。

def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])


# 測試總是要乾淨且獨立的環境，且不希望會有互相干擾的依賴情形。
# 因此對於相似的測試，就需要每次初始化一次需要的設定。  -> setUp()
# 甚至有每個方法結束後的清理功能。  -> tearDown()

# part1 程式部分。
from stats import StatsList


# part2 測試部分：
class TestValidInputs(unittest.TestCase):
    # 複寫setUp方法，讓每次test時都會呼叫，達到初始化的作用。
    def setUp(self):
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_mode(self):
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.append(2)
        self.assertEqual(self.stats.mode(), [2])


# python 的 discover 模組。
# 他可以在目前的目錄或是子目錄搜尋是否有test開頭的名稱，如果有的話，並且是TestCase的物件，就會執行測試。
# python -m unittest discover

# 忽略失敗的測試或是不想要測試的測試。
# 有時候已知測試會失敗，不想要測試。 甚至是要特定版本才能做測試。 也有可能要在某個作業系統下才需要測試。
# expectedFailure(), skip(reason), skipIf(condition, reason), skipUnless(condition, reason)
import sys


class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless.")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 4, "broken on 3.4")
    def test_skipIf(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'), "broken unless on linux.")
    def test_skipunless(self):
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()

