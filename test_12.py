import random
import pprint


def test():
    pupils_task = []
    quantity = 0
    while quantity < 15:
        first = random.randint(2, 9)
        second = random.randint(2, 9)
        if '%d * %d' % (first, second) in pupils_task or '%d * %d' % (second, first) in pupils_task:
            continue
        expression = '%d * %d' % (first, second)
        pupils_task.append(expression)
        quantity += 1
    pprint.pprint(pupils_task)
    return pupils_task


test()