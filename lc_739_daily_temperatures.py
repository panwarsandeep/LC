class Solution:
    def dailyTemperatures(self, T):
        res = [0]*len(T)
        stack = []
        tl = len(T)
        i = 0
        while True:
            if i >= tl - 1:
                break

            while i < tl - 1 and T[i+1] > T[i]:
                res[i] = 1
                print(i, T[i],T[i+1])
                while stack and T[i] > T[stack[-1]]:
                    v = stack.pop()
                    print("ind", i, v)
                    res[v] = i - v
                i += 1

            while stack and T[i] > T[stack[-1]]:
                v = stack.pop()
                print("ind", i, v)
                res[v] = i - v
            stack.append(i)
            i += 1
            print(stack)
        return res

if __name__ == '__main__':
    sol = Solution()
    
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    r = sol.dailyTemperatures(T)
    print(r)