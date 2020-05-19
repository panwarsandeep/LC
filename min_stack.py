class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []
        

    def push(self, x: int) -> None:
        
        if self.min == None or self.min > x:
            self.min = x
        self.stack.append([x,self.min])

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.min = None
        else:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
obj = None
cmd = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
par = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

cmd = ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
par = [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
for i in range(len(cmd)):
    if cmd[i] == "MinStack":
        obj = MinStack()
        print(None, cmd[i])
    if cmd[i] == "getMin":
        print(obj.getMin(), cmd[i], obj.stack)
    elif cmd[i] == "push":
        print(obj.push(par[i]), cmd[i], par[i])
    elif cmd[i] == "pop":
        print(obj.pop(), cmd[i])
    elif cmd[i] == "top":
        print(obj.top(), cmd[i])
    else:
        pass

# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()