

class VectorClock:
    def generate(self, n):
        return (0,) * n

    def compare(self, a, b):
        gt = False
        lt = False

        for j, k in zip(a, b):
            gt |= j > k
            lt |= j < k
            if gt and lt:
                break
        return int(gt) - int(lt)

    def is_concurrent(self, a, b):
        return (a != b) and self.compare(a, b) == 0

    def increment(self, clock, index):
        return clock[:index] + (clock[index] + 1,) + clock[index+1:]

    def merge(self, a, b):
        return tuple(map(max, zip(a, b)))
