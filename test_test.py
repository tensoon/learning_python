import sched, time
from datetime import datetime

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    print(datetime.now(), "doing stuff")
    # do your stuff
    s.enter(1, 1, do_something, (sc,))


s.enter(1, 1, do_something, (s,))
s.run()
