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

    def draw(self, count):
        cnt = count if count <= len(self.contents) else len(self.contents)
        result = []
        for i in range(cnt):
            # random...
            rnd = random.randrange(len(self.contents))
            result.append(self.contents[rnd])
            self.contents.pop(rnd)
        return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass