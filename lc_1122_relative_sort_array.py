from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1, arr2):
        smap = {}
        l = len(arr2)
        for i, n in enumerate(arr2):
            print(n, i)
            smap[n] = i
        for i in range(1001):
            if i in smap:
                continue
            smap[i] = l + i
        return sorted(arr1, key=lambda x: smap[x])

if __name__ == '__main__':
    sol = Solution()

    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    r = sol.relativeSortArray(arr1, arr2)
    print(r)