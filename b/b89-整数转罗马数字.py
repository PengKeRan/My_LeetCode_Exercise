class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        num_str = str(num)
        n = len(num_str)
        for i in range(n):
            digit = int(num_str[i])
            if n - i == 4:
                for _ in range(digit):
                    ans += "M"
            if n - i == 3:
                if digit == 9:
                    ans += "CM"
                elif digit == 8:
                    ans += "DCCC"
                elif digit == 7:
                    ans += "DCC"
                elif digit == 6:
                    ans += "DC"
                elif digit == 5:
                    ans += "D"
                elif digit == 4:
                    ans += "CD"
                elif digit == 3:
                    ans += "CCC"
                elif digit == 2:
                    ans += "CC"
                elif digit == 1:
                    ans += "C"
                else:
                    continue

            if n - i == 2:
                if digit == 9:
                    ans += "XC"
                elif digit == 8:
                    ans += "LXXX"
                elif digit == 7:
                    ans += "LXX"
                elif digit == 6:
                    ans += "LX"
                elif digit == 5:
                    ans += "L"
                elif digit == 4:
                    ans += "XL"
                elif digit == 3:
                    ans += "XXX"
                elif digit == 2:
                    ans += "XX"
                elif digit == 1:
                    ans += "X"
                else:
                    continue
            if n - i == 1:
                if digit == 9:
                    ans += "IX"
                elif digit == 8:
                    ans += "VIII"
                elif digit == 7:
                    ans += "VII"
                elif digit == 6:
                    ans += "VI"
                elif digit == 5:
                    ans += "V"
                elif digit == 4:
                    ans += "IV"
                elif digit == 3:
                    ans += "III"
                elif digit == 2:
                    ans += "II"
                elif digit == 1:
                    ans += "I"
                else:
                    continue

        return ans


num = 3749
print(Solution().intToRoman(num))  # MMMDCCXLIX
