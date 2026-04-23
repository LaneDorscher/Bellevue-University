def philosopher(i):
    while True:
        think()
        if i % 2 == 0:
            pick_up(left_fork(i))
            pick_up(right_fork(i))
        else:
            pick_up(right_fork(i))
            pick_up(left_fork(i))
        eat()
        put_down(left_fork(i))
        put_down(right_fork(i))


def put_down(var):
    pass
def pick_up(var):
    pass
def left_fork(var):
    pass
def right_fork(var):
    pass
def think():
    pass
def eat():
    pass