from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cmap = defaultdict(int)

        tot = len(s)
        for c in s:
            cmap[c] += 1
        for c in t:
            if cmap[c] <= 0:
                return False
            cmap[c] -= 1
            tot -= 1
        if tot > 0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()

    s = "anagram"
    t = "nagaram"
    r = sol.isAnagram(s, t)
    print(r)