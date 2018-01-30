import logging
import itertools
import bisect
import random
from threading import Timer

util_logger = logging.getLogger(__name__)

# stack overflow
class RepeatedTimer(object):
    def __init__(self, interval, iterations, function, db):
        self.logger     = logging.getLogger(__name__)
        self._timer     = None
        self.interval   = interval
        self.iterations = iterations
        self.counter    = 0
        self.function   = function
        self.db         = db
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.start()
        self.function(self.db)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
            self.counter = self.counter + 1
        else:
            self.stop()

    def stop(self):
        self._timer.cancel()
        self.is_running = False


#
# need to test this
# TODO: the choices() in random 3.6 is part of an object (not sure how this could break things
#
def choices(population, weights=None, *, cum_weights=None, k=1):
    """Return a k sized list of population elements chosen with replacement.

    If the relative weights or cumulative weights are not specified,
    the selections are made with equal probability.

    """
    if cum_weights is None:
        if weights is None:
            _int = int
            total = len(population)
            return [population[_int(random.random() * total)] for i in range(k)]
        cum_weights = list(itertools.accumulate(weights))
    elif weights is not None:
        raise TypeError('Cannot specify both weights and cumulative weights')
    if len(cum_weights) != len(population):
        raise ValueError('The number of weights does not match the population')
    total = cum_weights[-1]
    return [population[bisect.bisect(cum_weights, random.random() * total)] for i in range(k)]
