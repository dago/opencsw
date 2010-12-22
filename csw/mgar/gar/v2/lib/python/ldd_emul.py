import common_constants
import os
import re
import logging
import configuration as c

RUNPATH = "runpath"
NEEDED_SONAMES = "needed sonames"
SONAME = "soname"

class LddEmulator(object):
  """A class to emulate ldd(1)

  Used primarily to resolve SONAMEs and detect package dependencies.
  """
  def __init__(self):
    self.runpath_expand_cache = {}
    self.runpath_origin_expand_cache = {}
    self.symlink_expand_cache = {}
    self.symlink64_cache = {}
    self.runpath_sanitize_cache = {}

  def ExpandRunpath(self, runpath, isalist, binary_path):
    """Expands a signle runpath element.

    Args:
      runpath: e.g. "/opt/csw/lib/$ISALIST"
      isalist: isalist elements
      binary_path: Necessary to expand $ORIGIN
    """
    key = (runpath, tuple(isalist))
    if key not in self.runpath_expand_cache:
      origin_present = False
      # Emulating $ISALIST and $ORIGIN expansion
      if '$ORIGIN' in runpath:
        origin_present = True
      if origin_present:
        key_o = (runpath, tuple(isalist), binary_path)
        if key_o in self.runpath_origin_expand_cache:
          return self.runpath_origin_expand_cache[key_o]
        else:
          if not binary_path.startswith("/"):
            binary_path = "/" + binary_path
          runpath = runpath.replace('$ORIGIN', binary_path)
      if '$ISALIST' in runpath:
        expanded_list  = [runpath.replace('/$ISALIST', '')]
        expanded_list += [runpath.replace('$ISALIST', isa) for isa in isalist]
      else:
        expanded_list = [runpath]
      expanded_list = [os.path.abspath(p) for p in expanded_list]
      if not origin_present:
        self.runpath_expand_cache[key] = expanded_list
      else:
        self.runpath_origin_expand_cache[key_o] = expanded_list
        return self.runpath_origin_expand_cache[key_o]
    return self.runpath_expand_cache[key]

  def ExpandSymlink(self, symlink, target, input_path):
    key = (symlink, target, input_path)
    if key not in self.symlink_expand_cache:
      symlink_re = re.compile(r"%s(/|$)" % symlink)
      if re.search(symlink_re, input_path):
        result = input_path.replace(symlink, target)
      else:
        result = input_path
      self.symlink_expand_cache[key] = result
    return self.symlink_expand_cache[key]

  def Emulate64BitSymlinks(self, runpath_list):
    """Need to emulate the 64 -> amd64, 64 -> sparcv9 symlink

    Since we don't know the architecture, we are adding both amd64 and
    sparcv9.  It should be safe - there are other checks that make sure
    that right architectures are in the right directories.
    """
    key = tuple(runpath_list)
    if key not in self.symlink64_cache:
      symlinked_list = []
      for runpath in runpath_list:
        for symlink, expansion_list in common_constants.SYSTEM_SYMLINKS:
          for target in expansion_list:
            expanded = self.ExpandSymlink(symlink, target, runpath)
            if expanded not in symlinked_list:
              symlinked_list.append(expanded)
      self.symlink64_cache[key] = symlinked_list
    return self.symlink64_cache[key]

  def SanitizeRunpath(self, runpath):
    if runpath not in self.runpath_sanitize_cache:
      self.runpath_sanitize_cache[runpath] = os.path.normpath(runpath)
    return self.runpath_sanitize_cache[runpath]

  def ResolveSoname(self, runpath_list, soname, isalist,
                    path_list, binary_path):
    """Emulates ldd behavior, minimal implementation.

    runpath: e.g. ["/opt/csw/lib/$ISALIST", "/usr/lib"]
    soname: e.g. "libfoo.so.1"
    isalist: e.g. ["sparcv9", "sparcv8"]
    path_list: A list of paths where the soname is present, e.g.
               ["/opt/csw/lib", "/opt/csw/lib/sparcv9"]

    The function returns the one path.
    """
    # Emulating the install time symlinks, for instance, if the prototype contains
    # /opt/csw/lib/i386/foo.so.0 and /opt/csw/lib/i386 is a symlink to ".",
    # the shared library ends up in /opt/csw/lib/foo.so.0 and should be
    # findable even when RPATH does not contain $ISALIST.
    original_paths_by_expanded_paths = {}
    for p in path_list:
      expanded_p_list = self.Emulate64BitSymlinks([p])
      # We can't just expand and return; we need to return one of the paths given
      # in the path_list.
      for expanded_p in expanded_p_list:
        original_paths_by_expanded_paths[expanded_p] = p
    # This debugging line is sometimes useful, but generates a lot of output.
    # logging.debug(
    #     "%s: looking for %s in %s",
    #     soname, runpath_list, original_paths_by_expanded_paths.keys())
    for runpath_expanded in runpath_list:
      if runpath_expanded in original_paths_by_expanded_paths:
        # logging.debug("Found %s",
        #               original_paths_by_expanded_paths[runpath_expanded])
        return original_paths_by_expanded_paths[runpath_expanded]


def ParseDumpOutput(dump_output):
  binary_data = {RUNPATH: [],
                 NEEDED_SONAMES: []}
  runpath = []
  rpath = []
  for line in dump_output.splitlines():
    fields = re.split(c.WS_RE, line)
    if len(fields) < 3:
      continue
    if fields[1] == "NEEDED":
      binary_data[NEEDED_SONAMES].append(fields[2])
    elif fields[1] == "RUNPATH":
      runpath.extend(fields[2].split(":"))
    elif fields[1] == "RPATH":
      rpath.extend(fields[2].split(":"))
    elif fields[1] == "SONAME":
      binary_data[SONAME] = fields[2]
  if runpath:
    binary_data[RUNPATH].extend(runpath)
  elif rpath:
    binary_data[RUNPATH].extend(rpath)

  # Converting runpath to a tuple, which is a hashable data type and can act as
  # a key in a dict.
  binary_data[RUNPATH] = tuple(binary_data[RUNPATH])
  # the NEEDED list must not be modified, converting to a tuple.
  binary_data[NEEDED_SONAMES] = tuple(binary_data[NEEDED_SONAMES])
  binary_data["RUNPATH RPATH the same"] = (runpath == rpath)
  binary_data["RPATH set"] = bool(rpath)
  binary_data["RUNPATH set"] = bool(runpath)
  return binary_data
