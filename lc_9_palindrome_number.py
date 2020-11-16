from collections import defaultdict
import math
class Solution:
    '''
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        no_digits = math.floor(math.log10(x)+1)
        base = 10 ** (no_digits - 1)
        while x >= 10:
            if x // base != x % 10:
                return False
            x -= (base * (x // base))
            base //= 100
            x //= 10
            no_digits -= 2
            if x < base:
                if x == 0:
                    return True
                x_digits = math.floor(math.log10(x)+1)
                leading_zeros = no_digits - x_digits
                while leading_zeros:
                    if x % 10 != 0:
                        return False
                    x //= 10
                    base //= 100
                    no_digits -= 2
                    leading_zeros -= 1
                
        return True
    
    '''
    #simple solution
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        if x == reverse or x == reverse//10:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    
    x = 1221
    #x = 10
    x = 313
    x = 1000021
    #x = 1001001
    '''
    x = 100121001
    x = 1001
    x = 10022201
    '''
    #x = 1000110001
    x = 1001
    x = 1010110101
    print(x)
    r = sol.isPalindrome(x)
    print(r)