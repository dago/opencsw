import logging
import os
import signal
import subprocess

class Error(Exception):
  """Generic error"""

class ShellError(Error):
  """Problem running a shell command."""

class TimeoutExpired(Error):
  pass

def TimeoutHandler(signum, frame):
  raise TimeoutExpired

class ShellMixin(object):

  def ShellCommand(self, args, quiet=False):
    logging.debug("Calling: %s", repr(args))
    stdout, stderr = None, None
    if quiet:
      process = subprocess.Popen(args,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
      stdout, stderr = process.communicate()
      retcode = process.wait()
    else:
      retcode = subprocess.call(args)
    if retcode:
      logging.critical(stdout)
      logging.critical(stderr)
      raise Error("Running %s has failed." % repr(args))
    return retcode

def ShellCommand(args, env=None, timeout=None,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE):
  logging.debug("Running: %s", args)
  proc = subprocess.Popen(args,
                          stdout=stdout,
                          stderr=stderr,
                          env=env,
                          preexec_fn=os.setsid,
                          close_fds=True)
  # Python 3.3 have the timeout option
  # we have to roughly emulate it with python 2.x
  if timeout:
    signal.signal(signal.SIGALRM, TimeoutHandler)
    signal.alarm(timeout)

  try:
    stdout, stderr = proc.communicate()
    signal.alarm(0)
  except TimeoutExpired:
    os.kill(-proc.pid, signal.SIGKILL)
    msg = "Process %s killed after timeout expiration" % args
    raise TimeoutExpired(msg)

  retcode = proc.wait()
  return retcode, stdout, stderr


