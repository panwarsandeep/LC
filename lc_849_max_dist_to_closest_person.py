import math
class Solution:
    def maxDistToClosest(self, seats) -> int:
        l = len(seats)
        dist = 0
        maxd = 0
        tmp = 0
        for i in range(l):
            dist += 1
            if seats[i] == 1:
                tmp += 1
                if dist != 0 and tmp >= 2:
                    dist //= 2
                elif dist != 0:
                    dist -= 1
                if maxd < dist:
                    maxd = dist
                dist = 0

        maxd = max(dist,maxd)
        return maxd


if __name__ == '__main__':
    s = [1,0,0,0,1,0,0,0,0,0,1]

    #s = [1,0,0,0,1]
    s = [0,0,1]
    sol = Solution()
    r = sol.maxDistToClosest(s)
    print(r)

