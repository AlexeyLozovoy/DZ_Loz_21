class IntSet:
    def __init__(self, data):
        self.data = data

    def sum(self):
        return sum(self.data)

    def avg(self):
        return sum(self.data) / len(self.data)

    def max(self):
        return max(self.data)

    def min(self):
        return min(self.data)



