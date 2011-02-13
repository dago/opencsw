import logging
import subprocess

class Error(Exception):
  "Generic error"

class ShellError(Error):
  "Problem running a shell command."

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
