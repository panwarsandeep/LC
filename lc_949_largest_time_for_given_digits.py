from collections import defaultdict
class Solution:
    def permute(self, arr, ind, res):
        if ind == len(arr):
            th = int(arr[0])*10 + int(arr[1])
            tm = int(arr[2])*10 + int(arr[3])
            if ((th <= 23 and tm <= 59)) and \
                (th > res[0] or \
                (th == res[0] and tm > res[1])):
                res[0] = th
                res[1] = tm
                res[2] = arr[:]
            return
        for i in range(ind, len(arr)):
            arr[i], arr[ind] = arr[ind], arr[i]
            self.permute(arr, ind + 1, res)
            arr[i], arr[ind] = arr[ind], arr[i]


    def largestTimeFromDigits(self, arr):
        res = [-1, -1, []]
        
        self.permute(arr, 0, res)
        if len(res[2]) < 4:
            return ''
        return "{}{}:{}{}".format(res[2][0], res[2][1], res[2][2], res[2][3])
   

if __name__ == '__main__':
    sol = Solution()
    
    a = [1,2,3,4]
    #a = [0, 4, 0, 0]
    a = [1,3, 5,6]
    a = [5, 5, 5, 5]
    a = [2, 0, 6, 6]
    a = [0, 0, 0, 0]
    a = [5, 5, 5, 5]
    print(a)
    res = [0, 0, '']
    #sol.permute(a, 0, res)
    #print(res)
    r = sol.largestTimeFromDigits(a)
    print(r)
    

