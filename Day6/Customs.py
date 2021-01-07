
class CustomForm:

    def __init__(self, group_size, answers):
        self.group_size = group_size
        self.answers = answers

    #def get_all_yes_answers

def read_file_yes(path):
    ret = []
    tmp = {}
    with open(path, 'r') as input:
        for line in input:
            if line == '\n':
                ret.append(tmp)
                tmp = {}
            else:
                line = [c for c in line.strip()]
                for c in line:
                    if not c in tmp:
                        tmp[c] = 1
                    else:
                        tmp[c] += 1
        if len(tmp) > 0:
            ret.append(tmp)
    return ret

def read_file_only_yes(path):
    ret = []
    tmp = {}
    with open(path, 'r') as input:
        group_size = 0
        for line in input:
            if line == '\n':
                f = CustomForm(group_size, tmp)
                ret.append(f)
                tmp = {}
                group_size = 0
            else:
                group_size += 1
                line = [c for c in line.strip()]
                for c in line:
                    if not c in tmp:
                        tmp[c] = 1
                    else:
                        tmp[c] += 1
    return ret

def yes_answers(path):
    answers = read_file_yes(path)
    print(answers)
    number_yes = 0
    for i in answers:
        number_yes += len(i)
    return number_yes

def all_yes_answers(path):
    forms = read_file_only_yes(path)
    result = 0
    for form in forms:
        print(form.group_size, form.answers)
        for key,val in form.answers.items():
            if val == form.group_size:
                result += 1
    return result




print(all_yes_answers('input.txt'))