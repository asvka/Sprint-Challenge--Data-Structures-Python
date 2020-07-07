class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.initial_point = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.initial_point] = item
            self.initial_point += 1
        if self.initial_point == self.capacity:
            self.initial_point = 0

    def get(self):
        return self.data
