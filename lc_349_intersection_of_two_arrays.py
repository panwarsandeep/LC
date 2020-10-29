from collections import defaultdict
class Solution:
    def intersection(self, nums1, nums2):
        nmap = defaultdict(int)
        res = []
        for n in nums1:
            nmap[n] = 1
        for n in nums2:
            if nmap[n] == 1:
                res.append(n)
                nmap[n] += 1
        return res

if __name__ == '__main__':
    sol = Solution()

    s = [1,2,2,1]
    t = [2,2]
    s = [4, 9, 5]
    t = [9, 4, 9, 8, 4]
    r = sol.intersection(s, t)
    print(r)