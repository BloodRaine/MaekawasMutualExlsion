class VectorClock:
    clock = ()

    def generate(self, n):
        self.clock = (0,) * n

    def compare(a, b):
        gt = False
        lt = False

        for j, k in zip(a, b):
            gt |= j > k
            lt |= j < k
            if gt and lt:
                break
        return int(gt) - int(lt)

    def is_concurrent(a, b):
        return (a != b) and self.compare(a, b) == 0

    def increment(clock, index):
        self.clock[:index] + (self.clock[index] + 1,) + self.clock[index+1:]

    def merge(a, b):
        return tuple(map(max, zip(a, b)))

VC = VectorClock
VC.generate(2)
print(VC.clock)