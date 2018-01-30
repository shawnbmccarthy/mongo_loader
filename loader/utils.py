import logging
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