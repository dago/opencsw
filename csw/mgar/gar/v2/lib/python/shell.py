import copy
import logging
import os
import pipes
import signal
import subprocess

from lib.python import errors

class ShellError(errors.Error):
  """Problem running a shell command."""


class TimeoutExpired(errors.Error):
  """Command running for too long."""


def TimeoutHandler(signum, frame):
  raise TimeoutExpired

def ShellCommand(args, env=None,
                 timeout=None,
                 quiet=True,
                 allow_error=False,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE):
  logging.debug("ShellCommand(%s)", " ".join(pipes.quote(x) for x in args))
  if not env:
    env = copy.copy(os.environ)

  env['LC_ALL'] = 'C'

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
    raise ShellError(
        'Running %r has failed, error code: %s. To find out why the command '
        'failed, please run it in the foreground, like this: %s'
        % (args, retcode, ' '.join(pipes.quote(x) for x in args)))

  return retcode, stdout, stderr

def MakeDirP(self, dir_path, exc_class=None):
  """mkdir -p equivalent.

  http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
  """
  try:
    os.makedirs(dir_path)
  except OSError as exc:
    if exc.errno == errno.EEXIST and os.path.isdir(dir_path):
      pass
    else:
      if exc_class:
        raise exc_class('cannot mkdir %s: %s' % (dir_path, exc))
      else:
        raise
