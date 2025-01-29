class MinStack:

    def __init__(self):
        self.arr=[]
        self.minArr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minArr == [] or val <= self.minArr[-1]:
            self.minArr.append(val)
        

    def pop(self) -> None:
        if self.arr == []:
            return
        if self.arr[-1] == self.minArr[-1]:
            self.minArr.pop()
        self.arr.pop()
        

    def top(self) -> int:
        if self.arr == []:
            return
        return self.arr[-1]
        

    def getMin(self) -> int:
        if self.minArr == []:
            return
        return self.minArr[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
