class Stack:
    def __int__(self):
        self.arr = []

    def push(self, val):
        self.arr = [val] + self.arr
        if len(self.mins) == 0:
            self.mins = [val]
        else:
            if self.mins[0] >= val:
                self.mins = [val]

    def pop(self):
        v = self.arr[0]
        self.arr = self.arr[1:]
        return v

    def min(self):
