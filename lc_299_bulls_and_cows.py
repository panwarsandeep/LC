from collections import defaultdict
class Solution:
    def getHint(self, secret, guess):
        sec_d = defaultdict(int)
        gue_d = defaultdict(int)
        no_a = 0
        no_b = 0
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                sec_d[int(secret[i])] += 1
                gue_d[int(guess[i])] += 1
            else:
                no_a += 1
        for i in range(10):
            if sec_d[i] and gue_d[i]:
                no_b += sec_d[i] if sec_d[i] <= gue_d[i] else gue_d[i]
        res = str(no_a)+"A"+str(no_b)+"B"
        return res


   

if __name__ == '__main__':
    sol = Solution()
    
    s = "1807"
    g = "7810"
    s = "1123"
    g = "0111"
    s = "1"
    g = "1"
    r = sol.getHint(s, g)
    print(r)
    

