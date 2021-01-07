
class EncodingError:

    def __init__(self, path):
        self.cipher_numbers = self.read_file(path)
        self.cipher_size = len(self.cipher_numbers)
        self.block_size = 0
        self.sum_cache = self.initialize_sum_cache()
        self.cache_hit = 0
        self.cache_miss = 0

    def read_file(self, path):
        ciphers = []
        with open(path, 'r') as input:
            for line in input:
                ciphers.append(int(line.strip()))
        return ciphers

    def initialize_sum_cache(self):
        size = self.cipher_size
        result = [[0 for i in range(size)] for j in range(size)]
        return result

    def crack_cipher(self, block_size):
        self.block_size = block_size
        # start by getting the sum of the first 25
        for i in range(self.block_size):
            for j in range((i+1),self.block_size):
                self.sum_cache[i][j] = self.cipher_numbers[i] + self.cipher_numbers[j]
        while(True):
            for i in range(self.block_size, self.cipher_size):
                (valid, num) = self.crack_cipher_helper((i - self.block_size), i - 1, self.cipher_numbers[i])
                if not valid:
                    print(self.cache_hit / self.cache_miss)
                    return num

    def crack_cipher_helper(self, start, end, number_in_question):
        for i in range(start, (end+1)):
            for j in range((i+1), (end+1)):
                print(str(i) + ": " + str(self.cipher_numbers[i]), str(j) + ": " + str(self.cipher_numbers[j]))
                if self.sum_cache[i][j] == 0:
                    self.cache_hit += 1
                    sum = self.cipher_numbers[i] + self.cipher_numbers[j]
                    self.sum_cache[i][j] = sum
                else:
                    self.cache_miss += 1
                    sum = self.sum_cache[i][j]
                print(sum)
                if sum == number_in_question:
                    return True, 0
        return False, number_in_question

    def find_cipher_sum(self, number):
        for i in range(self.cipher_size):
            sum = self.cipher_numbers[i]
            for j in range(i+1, self.cipher_size):
                if self.sum_cache[i][j] == 0:
                    # we should assume that all entries up to this point have been cached, or we are at a 'new' i
                    self.cache_miss += 1
                    sum += self.cipher_numbers[j]
                    self.calc_sum_cache(i, j, sum)
                else:
                    self.cache_hit += 1
                    sum = self.sum_cache[i][j]
                    self.calc_sum_cache(i, j, sum)
                if sum == number:
                    print(self.cache_hit / self.cache_miss)
                    result_set = self.cipher_numbers[i:j+1]
                    result_set.sort()
                    return result_set[0] + result_set[-1]
                elif sum > number:
                    break
                else:
                    continue


    # We want to try to use this opportunity to calculate the 'next' cache needed.
    def calc_sum_cache(self, i, j, sum):
        self.sum_cache[i][j] = sum
        if not (j - 1) <= i:
            self.sum_cache[i+1][j] = self.sum_cache[i+1][j-1] + self.cipher_numbers[j]
        else:
            self.sum_cache[i+1][j] = self.cipher_numbers[j]


e = EncodingError('input.txt')
#print(e.crack_cipher(25))
print(e.find_cipher_sum(36845998))
#print(e.find_cipher_sum(127))
#36845998