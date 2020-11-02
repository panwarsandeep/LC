import bisect
class Solution:
    def findRightInterval(self, intervals):
        tmp_list = sorted([[x[0], i] for i, x in enumerate(intervals)], key=lambda x: x[0])

        res = []
        sorted_ind = [x[0] for x in tmp_list]
        for num in intervals:
            bi = bisect.bisect_left(sorted_ind, num[1])
            if bi == len(sorted_ind):
                bi -= 1
            if tmp_list[bi][0] >= num[1]:
                res.append(tmp_list[bi][1])
            else:
                res.append(-1)
        return res


if __name__ == '__main__':
    sol = Solution()


    intervals = [[3,4],[2,3],[1,2]]
    intervals = [[1,4],[2,3],[3,4]]
    print(intervals)
    r = sol.findRightInterval(intervals)
    print(r)