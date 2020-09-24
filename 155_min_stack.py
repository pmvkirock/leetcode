class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minele=0
        self.stack=[]

    def push(self, x: int) -> None:
        if self.stack==[]:
            self.stack.append(x)
            self.minele=x
        else:
            if x<self.minele:
                self.stack.append(2*x-self.minele)
                self.minele=x
            else:
                self.stack.append(x)


    def pop(self) -> None:
        if self.stack[-1]<self.minele:
            self.minele=2*self.minele-self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()


    def top(self) -> int:
        if self.stack[-1]<self.minele:
            return self.minele
        else:
            return self.stack[-1]


    def getMin(self) -> int:
        return self.minele

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()