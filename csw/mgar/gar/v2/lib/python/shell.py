import logging
import subprocess

class Error(Exception):
  "Generic error"

class ShellError(Error):
  "Problem running a shell command."

class ShellMixin(object):

  def ShellCommand(self, args, quiet=False):
    logging.debug("Calling: %s", repr(args))
    if quiet:
      process = subprocess.Popen(args,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
      stdout, stderr = process.communicate()
      retcode = process.wait()
    else:
      retcode = subprocess.call(args)
    if retcode:
      raise Error("Running %s has failed." % repr(args))
    return retcode
