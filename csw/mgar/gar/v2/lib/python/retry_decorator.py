# From: https://gist.github.com/hoffmann/470611
# With small changes.

import time
import logging

class Retry(object):
  default_exceptions = (Exception,)
  def __init__(self, tries, exceptions=None, delay=0, logger=None):
    """Decorator for retrying function if exception occurs

    Args:
      tries: num tries
      exceptions: exceptions to catch
      delay: wait seconds between retries
    """
    self.tries = tries
    self.exceptions = exceptions
    if self.exceptions is None:
      self.exceptions = Retry.default_exceptions
    self.delay = delay
    self.logger=logger

  def __call__(self, f):
    def fn(*args, **kwargs):
      last_exception = None
      for _ in range(self.tries):
        try:
          return f(*args, **kwargs)
        except self.exceptions as e:
          msg = "Retry, exception: "+str(e)
          if self.logger:
            self.logger.info(msg)
          else:
            logging.info(msg)
          time.sleep(self.delay)
          last_exception = e
      # If no success after all tries, raise last exception.
      raise last_exception
    return fn
