
class Password:

    def __init__(self, char: str, high: int, low: int, password_list: list):
        self.char = char
        self.high = high
        self.low = low
        self.password_list = password_list

    def get_char(self):
        return self.char

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_password_list(self):
        return self.password_list

    def get_char_count(self):
        return self.password_list.count(self.char)

    def char_count_as_expected(self):
        if self.low <= self.get_char_count() <= self.high:
            print(self.low, self.get_char_count(), self.high, ''.join(self.password_list))
            return True
        else:
            #print(self.low, self.get_char_count(), self.high, ''.join(self.password_list))
            return False

    def in_exactly_one_required_position(self):
        if self.password_list[(self.low - 1)] == self.char or self.password_list[(self.high - 1)] == self.char:
            if self.password_list[(self.low - 1)] == self.char and self.password_list[(self.high - 1)] == self.char:
                return False
            else:
                print(self.low, self.high, ''.join(self.password_list))
                return True
        else:
            return False


def read_file(path):
    ret = []
    with open(path, 'r') as input:
        for line in input:
            ret.append(line)
    return ret


def parse_pwd_string(line: str):
    l = line.split(' ')
    (low, high) = l[0].split('-')
    char = l[1][0]
    char_list = [c for c in l[2].strip()]
    return Password(char, int(high), int(low), char_list)


def count_correct_pwds(path):
    count = 0
    for i in read_file(path):
        p = parse_pwd_string(i)
        #print(p.get_low(), p.get_high(), p.get_char(), p.get_password_list())
        if p.char_count_as_expected():
            count = count + 1
    return count


def count_correct_pwds_2(path):
    count = 0
    for i in read_file(path):
        p = parse_pwd_string(i)
        #print(p.get_low(), p.get_high(), p.get_char(), p.get_password_list())
        if p.in_exactly_one_required_position():
            count = count + 1
    return count


#print(count_correct_pwds('input.txt'))
print(count_correct_pwds_2('input.txt'))

