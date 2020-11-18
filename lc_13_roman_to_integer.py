from collections import defaultdict
import math
class Solution:
    def romanToInt(self, s):
        num = 0
        roman = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        next_mul = 1
        for i in range(len(s)-1, 0, -1):
            num = num + (roman[s[i]] * next_mul)
            if roman[s[i]] <= roman[s[i-1]]:
                next_mul = 1
            else:
                next_mul = -1
            
        num = num + roman[s[0]] * next_mul
        return num

if __name__ == '__main__':
    sol = Solution()
    
    s = "LVIII"
    s = "MCMXCIV"
    s = "V"
    print(s)
    r = sol.romanToInt(s)
    print(r)