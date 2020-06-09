

from collections import OrderedDict
class Solution:
    def findReplaceString(self, S, ind, src, tar) -> str:
        res = ""
        si = 0
        tl = 0
        map = {}
        for i, v in enumerate(ind):
            map[v] = [src[i], tar[i]]
        map = OrderedDict(sorted(map.items())) 
    
        for v, st in map.items():
            res += S[si + tl:v]
            if S[v:v + len(st[0])] == st[0]:
                res += st[1]
                tl = len(st[0])
            else:
                tl = 0
            si = v
        res += S[si+tl:]

        return res

if __name__ == '__main__':
    sol = Solution()

    s = "abcd"
    ind = [0,2]
    src = ["a","cd"]
    tar = ["eee","ffff"]
    
    s = "abcd"
    ind = [0,2]
    src = ["ab","ec"]
    tar = ["eee","ffff"]
    '''

    s = "vmokgggqzp"
    ind = [3,5,1]
    src = ["kg","ggq","mo"]
    tar = ["s","so","bfr"]
    '''
    s = "jjievdtjfb"
    ind = [4,6,1]
    src = ["md","tjgb","jf"]
    tar = ["foe","oov","e"]
    
    r = sol.findReplaceString(s, ind, src, tar)
    print(r)