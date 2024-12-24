# 383. 赎金信

from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_counter = Counter(magazine)
        for ch in ransomNote:
            mag_counter[ch] -= 1
            if mag_counter[ch] < 0:
                return False
        return True
