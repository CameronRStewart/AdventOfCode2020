def read_file(path):
    nums = []
    with open(path, 'r') as input:
        for line in input:
            nums.append(int(line))
    return nums


def find_2020_pair(path):
    nums = read_file(path)
    for i in nums:
        num_to_seek = 2020 - i
        if num_to_seek in nums:
            return i * num_to_seek


def find_2020_triplet(path):
    nums = read_file(path)
    nums.sort()
    index_i = 0
    for i in nums:
        index_j = index_i + 1
        for j in nums[index_j:]:
            if i + j > 2020:
                break
            index_k = index_j + 1
            for k in nums[index_k:]:
                print(i, j, k, i+j+k)
                if i + j + k == 2020:
                    return i * j * k
                elif i + j + k < 2020:
                    continue
                else:
                    break
        index_i = index_i + 1


print(find_2020_pair('input.txt'))
print(find_2020_triplet('input.txt'))
