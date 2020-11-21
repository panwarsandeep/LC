from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, para, banned):
        wdict = defaultdict(int)
        bdict = {}
        wcnt = 0
        mwrd = ""
        for b in banned:
            bdict[b] = True
        
        wlist = re.sub("[^\w]", " ",  para).split()
        for w in wlist:
            tw = w.lower()
            if not bdict.get(tw, None):
                wdict[tw] += 1
                if wdict[tw] > wcnt:
                    wcnt = wdict[tw]
                    mwrd = tw
        return mwrd
        
        
        

if __name__ == '__main__':
    sol = Solution()
    
    para = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    para = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    print(para, banned)
    r = sol.mostCommonWord(para, banned)
    print(r)