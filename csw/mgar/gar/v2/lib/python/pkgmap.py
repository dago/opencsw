#!/usr/bin/env python2.6

import re
import os

from lib.python import representations
from lib.python import struct_util

class Pkgmap(object):
  """Represents the pkgmap of the package.

  The plan:

    entries = [
      {
        'path': ...,
        'class': ...,
        (more fields?)
      }, ...
    ]

  + indexes
  """
  ENTRY_TYPES = {
      "1": "header (?)",
      "d": "directory",
      "f": "file",
      "s": "symlink",
      "l": "link",
      "i": "script",
      "e": "editable file",
      "p": "pipe"
  }

  def __init__(self, input, permissions=False,
               strip=None, basedir=""):
    self.paths = set()
    self.analyze_permissions = permissions
    self.entries = []
    self.classes = None
    self.strip = strip
    self.basedir = basedir
    for line in input:
      entry, line_to_add = self._ParseLine(line)
      # Relocatable packages support
      if entry.path:
        entry = entry._asdict()
        entry["path"] = os.path.join(basedir, entry["path"])
        # basedir here does not include the leading slash, but in pkgmap we
        # do need it.
        if not entry["path"].startswith("/"):
          entry["path"] = "/" + entry["path"]
        entry = representations.PkgmapEntry(**entry)
      self.entries.append(entry)
      if line_to_add:
        self.paths.add(line_to_add)
    self.entries_by_line = struct_util.IndexNamedtuplesBy(self.entries, "line")
    self.entries_by_type = struct_util.IndexNamedtuplesBy(self.entries, "type_")
    self.entries_by_class = struct_util.IndexNamedtuplesBy(self.entries, "class_")
    self.entries_by_path = struct_util.IndexNamedtuplesBy(self.entries, "path")
    self.entries = sorted(self.entries, key=lambda x: x.path)

  def _ParseLine(self, line):
    fields = re.split(r'\s+', line)
    if self.strip:
      strip_re = re.compile(r"^%s" % strip)
      fields = [re.sub(strip_re, "", x) for x in fields]
    line_to_add = None
    installed_path = None
    prototype_class = None
    line_type = fields[1]
    mode = None
    user = None
    group = None
    target = None
    if len(fields) < 2:
      return None
    elif line_type in ('f', 'd', 'p'):
      # Files and directories
      line_to_add = fields[3]
      installed_path = fields[3]
      prototype_class = fields[2]
      if self.analyze_permissions:
        line_to_add += " %s %s %s" % tuple(fields[4:7])
      mode, user, group = fields[4:7]
    elif line_type in ('e'):
      # Editable files
      line_to_add = fields[3]
      installed_path = fields[3]
      prototype_class = fields[2]
    elif line_type in ('s', 'l'):
      # soft- and hardlinks
      # This breaks if PAX is broken. A rare case, but can happen.
      if "=" not in fields[3]:
        line_to_add = "broken link entry: %s" % fields[3]
      else:
        link_from, link_to = fields[3].split("=")
        installed_path = link_from
        line_to_add = "%s --> %s" % (link_from, link_to)
        target = struct_util.ResolveSymlink(link_from, link_to)
        prototype_class = fields[2]
    if line_to_add:
      self.paths.add(line_to_add)

    # entry = {
    #     "line": line.strip(),
    # }
    # 'line, class_, mode, owner, group, path, target, type_, '
    # 'major, minor, size, cksum, modtime, pkgnames')
    entry = representations.PkgmapEntry(
        line=line.strip(),
        class_=prototype_class,
        mode=mode,
        owner=user,
        group=group,
        path=installed_path,
        target=target,
        type_=line_type,
        major=None,
        minor=None,
        size=None,
        cksum=None,
        modtime=None,
        pkgnames=[])

    return entry, line_to_add

  def GetClasses(self):
    """The assumtion is that the set of classes never changes."""
    if not self.classes:
      self.classes = set()
      for entry in self.entries:
        if entry["class"]:  # might be None
          self.classes.add(entry["class"])
    return self.classes
