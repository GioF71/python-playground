import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, \
            red = 0, \
            blue = 0, \
            green = 0, \
            yellow = 0, \
            test = 0):
        self.by_color = {}
        self.by_color["red"] = red
        self.by_color["blue"] = blue
        self.by_color["green"] = green
        self.by_color["yellow"] = yellow
        self.by_color["test"] = test
        color_list = []
        color_list.append(("red", red))
        color_list.append(("blue", blue))
        color_list.append(("green", green))
        color_list.append(("yellow", yellow))
        color_list.append(("test", test))
        sList = sorted(color_list, key = lambda x: x[1], reverse = True)
        result = []
        for item in sList:
            cnt = item[1]
            for x in range(cnt):
                result.append(item[0])
        self.contents = result



def compare_array(item1, item2):
    if item1[1] > item2[1]:
        return -1
    elif item1[1] < item2[1]:
        return +1
    return 0


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass