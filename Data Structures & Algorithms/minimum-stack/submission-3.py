class MinStack:

    def __init__(self):
        self.main_list = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.main_list.append(val)
        if len(self.min_list) == 0:
            self.min_list.append(val)
        elif val <= self.min_list[-1]:
            self.min_list.append(val)
        

    def pop(self) -> None:
        value = self.main_list.pop()
        if value == self.min_list[-1]:
            self.min_list.pop()
        

    def top(self) -> int:
        return self.main_list[-1]
        

    def getMin(self) -> int:
        return self.min_list[-1]
        
