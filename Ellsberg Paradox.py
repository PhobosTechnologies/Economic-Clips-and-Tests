import random

urn = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
       'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def r_balls():
    balls = ['B', 'Y']
    return random.choice(balls)


urn[30:90] = [r_balls() for amb in urn[30:90]]


def count_x(lst, x):
    return lst.count(x)


for x in ['R', 'B', 'Y']:
    print('{} occurs {} times'.format(x, count_x(urn, x)))


# for amb in urn[30:90]:
    # amb = random.randint(1, 50)
    # r_balls = ['B', 'Y']
    # random.choice(r_balls)
    # print(random.randint(1, 50))

# for amb in urn:
#     print(amb)
