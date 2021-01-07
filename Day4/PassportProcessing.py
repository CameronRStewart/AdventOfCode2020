# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
import re

eye_colors = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]


def check_hgt(x):
    p = re.match(r"(\d*)(in|cm)$", x)
    if p is not None:
        num = p.group(1)
        unit = p.group(2)
        if unit == 'cm':
            if 150 <= int(num) <= 193:
                return True
            else:
                return False
        elif unit == 'in':
            if 59 <= int(num) <= 76:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


class PassportProcessing:

    def __init__(self, path):
        self.passports = self.read_file(path)
        self.required_fields = {
            "byr": (lambda x: len(x) == 4 and 1920 <= int(x) <= 2002),
            "iyr": (lambda x: len(x) == 4 and 2010 <= int(x) <= 2020),
            "eyr": (lambda x: len(x) == 4 and 2020 <= int(x) <= 2030),
            "hgt": (lambda x: check_hgt(x)),
            "hcl": (lambda x: re.fullmatch(r"#([A-Za-z0-9]{6})", x) is not None),
            "ecl": (lambda x: x in eye_colors),
            "pid": (lambda x: re.fullmatch(r"[0-9]{9}", x))
        }

    def read_file(self, path):
        ret = []
        tmp = {}
        with open(path, 'r') as input:
            for line in input:
                if line == '\n':
                    ret.append(tmp)
                    #print(tmp)
                    tmp = {}
                else:
                    for i in line.split(' '):
                        (key, val) = i.strip().split(':')
                        tmp[key.lower()] = val
        return ret

    def check_required_fields(self, passport):
        if len(passport) < 7:
            return False
        required_keys = self.required_fields.keys()
        for key in required_keys:
            if not key in passport:
                return False
            else:
                # Validate values
                validation = self.required_fields[key]
                if not validation(passport[key]):
                    return False
        return True

    def validate_passports(self):
        valid = 0
        for passport in self.passports:
            if self.check_required_fields(passport):
                valid += 1
        return valid


p = PassportProcessing('input.txt')
print(p.validate_passports())