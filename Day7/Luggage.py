import re
# dim orange bags contain 1 mirrored lavender bag, 2 shiny bronze bags, 5 posh gray bags, 3 striped green bags
# {"dim orange": {"mirrored lavendar": 1, "shiny bronze": 2, "posh gray": 5, "striped green": 3}}
# no other bags is a special case
class Luggage:

    def __init__(self, path):
        self.bags_contain = {}
        self.color_contained_cache = {}
        self.read_file(path)

    def read_file(self, path):
        with open(path, 'r') as input:
            for line in input:
                (name, contains) = self.parse_bag(line)
                self.bags_contain[name] = contains
        #print(self.bags_contain)

    def parse_bag(self, bag):
        #print(bag.strip())
        contains = {}
        matches = re.match(r"^(.*) bags contain (.*)\.", bag)
        name = matches.group(1)
        contents = matches.group(2).split(",")
        #print(contents)
        for c in contents:
            if c.strip() == 'no other bags':
                contains = {}
            else:
                content_matches = re.match(r"^\ ?(\d*) (.*) bags?", c)
                count = content_matches.group(1)
                bag_type = content_matches.group(2)
                contains[bag_type] = int(count)
        return name, contains

    def contains_color(self, color):
        count = 0
        for name, i in self.bags_contain.items():
            if color in i:
                self.color_contained_cache[name] = True
                count += 1
            elif name in self.color_contained_cache and self.color_contained_cache[name] == True:
                count += 1
            elif self.color_container_helper(color, name, i):
                self.color_contained_cache[name] = True
                count += 1
            else:
                pass
        return count

    def color_container_helper(self, wanted_color, containing_bag_name, bag_types):
        if self.check_cache(wanted_color, containing_bag_name):
            return True
        elif wanted_color in bag_types:
            self.color_contained_cache[containing_bag_name] = True
            return True
        else:
            for bag_type in bag_types:
                if self.color_container_helper(wanted_color, bag_type, self.bags_contain[bag_type]):
                    return True
            return False

    def check_number_of_bags_contained(self, bag_list):
        total = 1
        print(bag_list)
        for bag, count in bag_list.items():
            total = total + count * self.check_number_of_bags_contained(self.bags_contain[bag])
            print(total)
        return total

    def check_cache(self, wanted_color, check_color):
        return wanted_color in self.color_contained_cache and self.color_contained_cache[check_color]


l = Luggage('input.txt')
#print(l.contains_color('shiny gold'))
print(l.check_number_of_bags_contained(l.bags_contain['shiny gold']))
#print(l.color_container_helper('shiny gold', 'light red', {"bright white": 1, "muted yellow": 2}))