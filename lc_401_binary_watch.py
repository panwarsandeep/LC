from collections import defaultdict
class Solution:
    def readBinaryWatch(self, num):
        def get_time(n):
            hourd = {x:bin(x).count('1') for x in range(0, 12)}
            mind = {x:bin(x).count('1') for x in range(0, 60)}
            for hour, hour_bit_cnt in hourd.items():
                for minute, minute_bit_count in mind.items():
                    if hour_bit_cnt + minute_bit_count == n:
                        t_time = "{:d}:{:02d}".format(hour, minute)
                        res.append(t_time)

        
        res = []
        get_time(num)
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 1
    
    r = sol.readBinaryWatch(n)
    print(r)