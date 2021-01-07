

class TobogganRide:

    def __init__(self, path):
        self.map = self.read_file(path)
        self.finish_distance = len(self.map)
        self.render_width = len(self.map[0]) - 1

    def read_file(self, path):
        ret = []
        with open(path, 'r') as input:
            for line in input:
                ret.append([c for c in line.strip()])
        return ret

    def move_next_index(self, i, j, delta_i, delta_j):
        next_i = i + delta_i
        next_j = j + delta_j
        if next_j > self.render_width:
            next_j = (next_j - self.render_width) - 1
        return (next_i, next_j)

    def is_tree(self, i, j):
        return self.map[i][j] == '#'

    def toboggan_ride(self, delta_i, delta_j):
        index_i = 0
        index_j = 0
        trees = 0
        while index_i < self.finish_distance:
            #print(self.map[index_i][index_j])
            if self.is_tree(index_i, index_j):
                trees += 1
            (index_i, index_j) = self.move_next_index(index_i, index_j, delta_i, delta_j)
        return trees


deltas = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
s = TobogganRide('input.txt')

result = 1
for i, j in deltas:
    result = result * s.toboggan_ride(i, j)
print(result)
