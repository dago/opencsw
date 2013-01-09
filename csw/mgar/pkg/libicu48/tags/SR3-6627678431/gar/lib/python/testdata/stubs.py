# $Id$

"""Stubs are used when mocks are an overkill.

These ones accept calls to specified methods.
"""

class LoggerStub(object):
  def debug(self, debug_s, *kwords):
    pass
  def info(self, debug_s, *kwords):
    pass
  def warning(self, debug_s, *kwords):
    pass

class MessengerStub(object):
  def Message(self, m):
    pass
  def OneTimeMessage(self, key, m):
    pass
  def SuggestGarLine(self, m):
    pass

