from collections import defaultdict
class Solution:
    def intersect(self, nums1, nums2) :
        larr = nums1 if len(nums1) > len(nums2) else nums2
        cmap = defaultdict(int)
        for v in larr:
            cmap[v] += 1
        sarr = nums1 if larr != nums1 else nums2
        res = []
        for v in sarr:
            if cmap[v] > 0:
                res.append(v)
                cmap[v] -= 1
        return res

if __name__ == '__main__':
    sol = Solution()

    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    r = sol.intersect(arr1, arr2)
    print(r)