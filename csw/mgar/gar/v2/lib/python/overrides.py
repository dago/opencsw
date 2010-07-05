# $Id$
# coding=utf-8

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

  def DoesApply(self, tag):
    """Figures out if this override applies to the given tag."""
    basket_a = {}
    basket_b = {}
    if self.pkgname:
      basket_a["pkgname"] = self.pkgname
      basket_b["pkgname"] = tag.pkgname
    if self.tag_info:
      basket_a["tag_info"] = self.tag_info
      basket_b["tag_info"] = tag.tag_info
    basket_a["tag_name"] = self.tag_name
    basket_b["tag_name"] = tag.tag_name
    return basket_a == basket_b


def ApplyOverrides(error_tags, overrides):
  """Filters out all the error tags that overrides apply to.

  O(N * M), but N and M are always small.
  """
  tags_after_overrides = []
  applied_overrides = set([])
  provided_overrides = set(copy.copy(overrides))
  for tag in error_tags:
    override_applies = False
    for override in overrides:
      if override.DoesApply(tag):
        override_applies = True
        applied_overrides.add(override)
    if not override_applies:
      tags_after_overrides.append(tag)
  unapplied_overrides = provided_overrides.difference(applied_overrides)
  return tags_after_overrides, unapplied_overrides
