class BootLoopRecursive:

    def __init__(self, path):
        self.ops = self.read_file(path)
        self.op_map = {
            'nop': getattr(self, 'no_op'),
            'acc': getattr(self, 'accumulate'),
            'jmp': getattr(self, 'jump'),
        }

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


    def fix_infinite_loop(self, my_index):
        end = False
        while not end:
            call = self.op_map[op['op']]
            if not call(op['direction'], op['count'], my_index):
                # we are in a loop
                # pop until you reach your first nop or jmp that hasn't yet been altered
                print(self.op_stack)
                pass
            else:
                self.op_stack.append([op, self.op_index])