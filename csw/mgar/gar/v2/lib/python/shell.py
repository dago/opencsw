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

def ShellCommand(args, env=None, timeout=None,
                 quiet=True, allow_error=False,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE):
  logging.debug("Running: %s", args)

  if not quiet:
    stdout = subprocess.STDOUT
    stderr = subprocess.STDOUT

  # Python 3.3 have the timeout option
  # we have to roughly emulate it with python 2.x
  if timeout:
    signal.signal(signal.SIGALRM, TimeoutHandler)
    signal.alarm(timeout)

  try:
    proc = subprocess.Popen(args,
                            stdout=stdout,
                            stderr=stderr,
                            env=env,
                            preexec_fn=os.setsid,
                            close_fds=True)
    stdout, stderr = proc.communicate()
    retcode = proc.wait()

    signal.alarm(0)

  except TimeoutExpired:
    os.kill(-proc.pid, signal.SIGKILL)
    msg = "Process %s killed after timeout expiration" % args
    raise TimeoutExpired(msg)

  if retcode and not allow_error:
    logging.critical(stdout)
    logging.critical(stderr)
    raise Error("Running %s has failed." % repr(args))

  return retcode, stdout, stderr
