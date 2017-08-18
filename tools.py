class TickProfiler:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def get_ticks(self):
        return self.count
