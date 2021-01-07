class JoltageAdapter:

    def __init__(self, path):
        self.adapters = self.read_file(path)

    def read_file(self, path):
        adapters = []
        with open(path, 'r') as input:
            for line in input:
                adapters.append(int(line.strip()))
        adapters.sort()
        return adapters

    def adapt_that_joltage(self):
        ones = 0
        threes = 1  # built in adapter for device is always 3 higher than highest adapter.
        previous_adapter_joltage = 0

        for i in self.adapters:
            diff = i - previous_adapter_joltage
            if diff > 3:
                exit("Problem")
            elif diff == 1:
                ones += 1
            elif diff == 3:
                threes += 1
            else:
                pass
            previous_adapter_joltage = i
        return ones * threes

    def distinct_adapter_combos(self):
        pass

j = JoltageAdapter('input.txt')
print(j.adapt_that_joltage())
