
class BootLoop:

    def __init__(self, path):
        self.accumulator = 0
        self.op_cache = []
        self.swapped_op_index = None
        self.already_swapped_ops_index = []
        self.op_index = 0
        self.op_map = {
            'nop': getattr(self, 'no_op'),
            'acc': getattr(self, 'accumulate'),
            'jmp': getattr(self, 'jump'),
        }
        self.ops = self.read_file(path)

    def no_op(self, direction, count, my_index):
        if self.check_loop(my_index):
            return False
        else:
            self.op_index = my_index + 1
            self.op_cache.append(my_index)
            return True

    def accumulate(self, direction, count, my_index):
        if self.check_loop(my_index):
            return False
        else:
            if direction == '-':
                self.accumulator -= count
            else:
                self.accumulator += count
            self.op_index = my_index + 1
            self.op_cache.append(my_index)
            return True

    def jump(self, direction, count, my_index):
        if self.check_loop(my_index):
            return False
        else:
            if direction == '-':
                self.op_index -= count
            else:
                self.op_index += count
            self.op_cache.append(my_index)
            return True

    def check_loop(self, op_index):
        if op_index in self.op_cache:
            return True
        else:
            return False

    def read_file(self, path):
        ops = []
        with open(path, 'r') as input:
            for line in input:
                line = line.strip().split(" ")
                op = line[0]
                #print(line[1])
                tmp = [dircount for dircount in line[1]]
                direction = tmp[0]
                count = int("".join((tmp[1:])))
                ops.append({"op": op, "direction": direction, "count": count})
        return ops

    def reset_swapped_index(self):
        if not self.swapped_op_index is None:
            self.ops[self.swapped_op_index]['op'] = self.swap_index_helper(self.ops[self.swapped_op_index]['op'])
            #print("Resetting swapped index,op: "+str(self.swapped_op_index)+", "+self.ops[self.swapped_op_index]['op'])

    def swap_index_helper(self, op_name):
        if op_name == 'nop':
            return 'jmp'
        else:
            return 'nop'

    def find_and_swap_next_op(self, last_swapped_index):
        if last_swapped_index is None:
            last_swapped_index = -1
        for i in range(last_swapped_index + 1, len(self.ops)):
            if self.ops[i]['op'] == 'jmp' or self.ops[i]['op'] == 'nop':
                self.swapped_op_index = i
                self.ops[i]['op'] = self.swap_index_helper(self.ops[i]['op'])
                print("Swapping index to "+str(i))
                return True
        return False

    def find_infinite_loop(self):
        loop = False
        while not loop:
            op = self.ops[self.op_index]
            call = self.op_map[op['op']]
            if not call(op['direction'], op['count'], self.op_index):
                loop = True
        return self.accumulator

    def fix_infinite_loop(self):
        end = False
        final_index = len(self.ops) - 1
        while not end:
            print("op index: "+str(self.op_index))
            print("op cache: "+str(self.op_cache))
            if self.op_index > final_index:
                end = True
            else:
                op = self.ops[self.op_index]
                call = self.op_map[op['op']]
                if not call(op['direction'], op['count'], self.op_index):
                    print("hit loop")
                    # Loop, reset op_index, swap last changed nop or jmp, swap next nop or jmp, move on.
                    last_swapped = self.swapped_op_index
                    self.reset_swapped_index()
                    self.find_and_swap_next_op(last_swapped)
                    self.accumulator = 0
                    self.op_index = 0
                    self.op_cache = []
        return self.accumulator




b = BootLoop('input.txt')
print(b.fix_infinite_loop())