class queue:
    def __init__(self, len = 5):
        self.len = len
        self.data = [1 for _ in range(self.len)]

    def push(self, value):
        self.data.insert(0, value)
        if len(self.data) >= self.len:
            self.data = self.data[:self.len]

    def check(self):
        if sum(self.data) == 0:
            return 0
        return 1

if __name__ == "__main__":
    q = queue()
    for i in range(10000):
        q.push(i)
