class MinStack:

    def __init__(self):
        """
        initialize your stack structure here.
        """
        self.stack = []
        self.mins = [float("inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)

        # update mins
        self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()

        # update mins 
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]