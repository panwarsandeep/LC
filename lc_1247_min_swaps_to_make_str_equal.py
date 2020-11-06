from functools import cmp_to_key
class Solution:
    def minimumSwap(self, s1, s2):
        if len(s1) != len(s2):
            return -1
        
        um = []
        ans = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                um.append((s1[i], s2[i]))
        if len(um) % 2 != 0:
            return -1
        
        cnt_x_y = um.count(('x', 'y'))
        cnt_y_x = um.count(('y', 'x'))
        ans += cnt_x_y // 2
        cnt_x_y %= 2
        ans += cnt_y_x // 2
        cnt_y_x %= 2
        if cnt_x_y == cnt_y_x:
            ans += cnt_x_y*2
            return ans
        return -1
        
        



if __name__ == '__main__':
    sol = Solution()

    s1 = "xx"
    s2 = "yy"
    s1 = "xy"
    s2 = "yx"
    #s1 = "xxyyxyxyxx"
    #s2 = "xyyxyxxxyx"
    r = sol.minimumSwap(s1, s2)
    print(r)