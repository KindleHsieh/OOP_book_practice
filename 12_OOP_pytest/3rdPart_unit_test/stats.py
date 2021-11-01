# -*- coding: utf-8 -*-
# author: Kindle Hsieh time: 2021/10/28
from typing import List, Optional
from collections import defaultdict


class StatsList(List[Optional[float]]):
    def mean(self) -> float:
        clean = list(filter(None, self))
        return sum(clean) / len(clean)

    def median(self) -> float:
        clean = list(filter(None, self))
        # odd.
        if len(clean) % 2:
            return clean[len(clean) // 2]
        # even.
        else:
            idx = len(clean) // 2
            return (clean[idx] + clean[idx - 1]) / 2

    def mode(self) -> List[float]:
        freqs: DefaultDict[float, int] = defaultdict(int)
        for item in filter(None, self):
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = [ item
            for item, value in freqs.items()
            if value == mode_freq
        ]
        return modes




