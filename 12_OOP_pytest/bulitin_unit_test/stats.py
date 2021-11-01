# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/28

from collections import defaultdict


class StatsList(list):
    def mean(self):
        return sum(self) / len(self)

    def median(self):
        # odd.
        if len(self) % 2:
            print(len(self) % 2)
            return self[int(len(self) / 2)]
        # even.
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx - 1]) / 2

    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freq:
                modes.append(item)
        return modes




