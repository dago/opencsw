# $Id$
# coding=utf-8

import re
import configuration as c

class CheckpkgTag(object):
  """Represents a tag to be written to the checkpkg tag file."""

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

  def ToGarSyntax(self):
    """Presents the error tag using GAR syntax."""
    msg_lines = []
    if self.msg:
      msg_lines.extend(textwrap(self.msg, 70,
                                initial_indent="# ",
                                subsequent_indent="# "))
    if self.tag_info:
      tag_postfix = "|%s" % self.tag_info.replace(" ", "|")
    else:
      tag_postfix = ""
    msg_lines.append(u"CHECKPKG_OVERRIDES_%s += %s%s"
                     % (self.pkgname, self.tag_name, tag_postfix))
    return "\n".join(msg_lines)


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
