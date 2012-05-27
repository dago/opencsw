# $Id$
# coding=utf-8

import re
import configuration as c

class CheckpkgTag(object):
  """Represents a tag to be written to the checkpkg tag file.

  This class is only used by submitpkg.  The main tag class lives in the
  models.py file.  The main difference is that this class does not need
  a database.
  """

  def __init__(self, pkgname, tag_name, tag_info=None, severity=None, msg=None):
    self.pkgname = pkgname
    self.tag_name = tag_name
    self.tag_info = tag_info
    self.severity = severity
    self.msg = msg

  def __repr__(self):
    return (u"CheckpkgTag(%s, %s, %s)"
            % (repr(self.pkgname),
               repr(self.tag_name),
               repr(self.tag_info)))

  def __eq__(self, other):
    value = (
        self.pkgname == other.pkgname
          and
        self.tag_name == other.tag_name
          and
        self.tag_info == other.tag_info
          and
        self.severity == other.severity
          and
        self.msg == other.msg)
    return value


def ParseTagLine(line):
  """Parses a line from the tag.${module} file.

  Returns a triplet of pkgname, tagname, tag_info.
  """
  level_1 = line.strip().split(":")
  if len(level_1) > 1:
    data_1 = ":".join(level_1[1:])
    pkgname = level_1[0]
  else:
    data_1 = level_1[0]
    pkgname = None
  level_2 = re.split(c.WS_RE, data_1.strip())
  tag_name = level_2[0]
  if len(level_2) > 1:
    tag_info = " ".join(level_2[1:])
  else:
    tag_info = None
  return (pkgname, tag_name, tag_info)
