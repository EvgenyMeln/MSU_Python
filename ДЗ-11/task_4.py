class GeomRangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
        self.started = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.started:
            self.started = True
            if self.current < self.stop:
                return self.current
            else:
                raise StopIteration

        self.current *= self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

class GeomRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 2
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 2
        else:
            self.start, self.stop, self.step = args
        
    def __iter__(self):
        return GeomRangeIterator(self.start, self.stop, self.step)

    def __getitem__(self, index):
        value = self.start * (self.step ** index)
        if value < self.stop:
            return value
        else:
            raise IndexError("index is out of the progression")

for x in GeomRange(1, 10, 2):
    print(x)

for x in GeomRange(1, 1, 2):
    print(x)

for x in GeomRange(1, 100, 3):
    print(x)
