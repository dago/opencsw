# $Id$
# coding=utf-8

"""Code related to overrides.

The override class is now in the models.py file, because it's one of the
SQLObject classes, with objects persisted in the database.
"""

import copy
import re
import configuration as c

def ParseOverrideLine(line):
  level_1 = line.split(":")
  if len(level_1) > 1:
    pkgname = level_1[0]
    data_1 = ":".join(level_1[1:])
  else:
    pkgname = None
    data_1 = level_1[0]
  level_2 = re.split(c.WS_RE, data_1.strip())
  if len(level_2) > 1:
    tag_name = level_2[0]
    tag_info = " ".join(level_2[1:])
  else:
    tag_name = level_2[0]
    tag_info = None
  return Override(pkgname, tag_name, tag_info)


class Override(object):
  """Represents an override of a certain checkpkg tag.

  It's similar to checkpkg.CheckpkgTag, but serves a different purpose.
  """

  def __init__(self, pkgname, tag_name, tag_info):
    self.pkgname = pkgname
    self.tag_name = tag_name
    self.tag_info = tag_info

  def __repr__(self):
    return (u"Override(%s, %s, %s)"
            % (repr(self.pkgname), repr(self.tag_name), repr(self.tag_info)))


def ApplyOverrides(error_tags, override_list):
  """Filters out all the error tags that overrides apply to.

  O(N * M), but N and M are always small.
  """
  tags_after_overrides = []
  applied_overrides = set([])
  provided_overrides = set(copy.copy(override_list))
  for tag in error_tags:
    override_applies = False
    for override in override_list:
      if override.DoesApply(tag):
        override_applies = True
        applied_overrides.add(override)
    if not override_applies:
      tags_after_overrides.append(tag)
  unapplied_overrides = provided_overrides.difference(applied_overrides)
  return tags_after_overrides, unapplied_overrides
