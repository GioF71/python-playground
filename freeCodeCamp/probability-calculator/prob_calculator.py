import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, count):
        cnt = min(count, len(self.contents))
        result = []
        for i in range(cnt):
            # random...
            rnd = random.randrange(len(self.contents))
            result.append(self.contents.pop(rnd))
        return result
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for experiment in range(num_experiments):
        current_hat = copy.deepcopy(hat)
        drawn = {}
        # start drawing balls
        list_drawn = current_hat.draw(num_balls_drawn)
        for current_drawn in list_drawn:
            drawn[current_drawn] = 1 if (not current_drawn in drawn) else drawn[current_drawn] + 1
        # check success
        exp_success = True
        for k,v in expected_balls.items():
            drawn_k = drawn[k] if k in drawn else 0
            enough = drawn_k >= v
            if enough == False: 
                exp_success = False
                break            
        if exp_success == True: success_count = success_count + 1
    return success_count / num_experiments