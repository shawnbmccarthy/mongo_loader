import logging
import itertools
import bisect
import random
from threading import Timer

util_logger = logging.getLogger(__name__)


class RepeatedTimer(object):
    """

    """
    def __init__(self, interval, iterations, func, db):
        """

        :param interval:
        :param iterations:
        :param func:
        :param db:
        """
        self.logger = logging.getLogger(__name__)
        self._timer = None
        self.interval = interval
        self.iterations = iterations
        self.counter = 0
        self.func = func
        self.db = db
        self.is_running = False

    def _run(self):
        """

        :return:
        """
        self.logger.debug('attempting to start function')
        self.is_running = False
        self.start()
        self.func(self.db)

    def start(self):
        """

        :return:
        """
        self.logger.debug('attempting to start')
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
            self.counter = self.counter + 1
        else:
            self.stop()

    def stop(self):
        """

        :return:
        """
        self.logger.debug('attempting to stop')
        self._timer.cancel()
        self.is_running = False


def choices(population, weights=None, *, cum_weights=None, k=1):
    """
    Return a k sized list of population elements chosen with replacement.

    If the relative weights or cumulative weights are not specified,
    the selections are made with equal probability.

    This emulates choices() which is found in the random module in 3.6

    """
    util_logger.debug('running choices')
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
