#!/opt/csw/bin/python2.6
# coding=utf-8
# vim:set sw=2 ts=2 sts=2 expandtab:

import tag
import os
import opencsw
import common_constants

class FileSetChecker(object):
  """Checks a file name set.

  Doesn't check anything about package contents.  The purpose of this
  class is to identify problems with the file set itself, e.g. an
  uncommitted package or a missing i386 package.
  """

  def _CheckUncommitted(self, files_with_metadata):
    tags = []
    expected_vendor_tag = "CSW"
    for filename, parsed_filename in files_with_metadata:
      if parsed_filename["vendortag"] != expected_vendor_tag:
        tags.append(tag.CheckpkgTag(
          None,
          "bad-vendor-tag",
          "filename=%s expected=%s actual=%s"
          % (filename,
             expected_vendor_tag,
             parsed_filename["vendortag"])))
    return tags

  def _CheckFilenames(self, files_with_metadata):
    tags = []
    for filename, parsed_filename in files_with_metadata:
      if not filename.endswith(".pkg.gz") and not filename.endswith(".pkg"):
        tags.append(tag.CheckpkgTag(
          None,
          "bad-filename",
          "filename=%s" % filename))
    return tags

  def _CheckMissingArchs(self, files_with_metadata):
    tags = []
    catalognames_by_arch = {}
    # We check all the OS releases that are included in the file set.
    # We won't report a missing i386-SunOS5.8 package if there was no
    # SunOS5.8 package in the set.
    osrels = set(x[1]["osrel"] for x in files_with_metadata)
    # Prepopulate sets, so that we have one set per each arch-osrel pair
    # that is applicable to this set of files.
    for arch in common_constants.PHYSICAL_ARCHITECTURES:
      for osrel in osrels:
        key = arch, osrel
        catalognames_by_arch[key] = set()
    # Assign files from the set to appropriate set.
    for file_path, file_metadata in files_with_metadata:
      catalogname = file_metadata["catalogname"]
      if file_metadata["arch"] == "all":
        archs = common_constants.PHYSICAL_ARCHITECTURES
      else:
        archs = [file_metadata["arch"]]
      osrel = file_metadata["osrel"]
      for arch in archs:
        key = arch, osrel
        if key in catalognames_by_arch:
          catalognames_by_arch[key].add(catalogname)
        else:
          tags.append(
              tag.CheckpkgTag(None,
                              "bad-arch-or-os-release",
                              "%s arch=%s osrel=%s" % (file_path, arch, osrel))
          )
    missing = {}
    for key1, set1 in catalognames_by_arch.iteritems():
      for catalogname in set1:
        for key2, set2 in catalognames_by_arch.iteritems():
          if catalogname not in set2:
            arch, osrel = key2
            missing_key = arch, osrel, catalogname
            missing.setdefault(missing_key, set()).add(
                "Because %s-%s-%s exists" % (catalogname, key1[0], key1[1]))
    for arch, osrel, catalogname in missing:
      error_tag_name = "%s-%s-missing" % (arch, osrel)
      tags.append(tag.CheckpkgTag(None, error_tag_name, catalogname))
    return tags

  def _FilesWithMetadata(self, file_list):
    files_with_metadata = []
    for file_path in file_list:
      pkg_path, basename = os.path.split(file_path)
      parsed = opencsw.ParsePackageFileName(basename)
      catalogname = parsed["catalogname"]
      files_with_metadata.append((basename, parsed))
      if parsed["arch"] == "all":
        archs = common_constants.PHYSICAL_ARCHITECTURES
      else:
        archs = [parsed["arch"]]
      for arch in archs:
        for osrel in common_constants.OS_RELS:
          key = arch, osrel
    return files_with_metadata

  def CheckFiles(self, file_list):
    """Checks a set of files. Returns error tags."""
    files_with_metadata = self._FilesWithMetadata(file_list)
    tags = []
    tags.extend(self._CheckMissingArchs(files_with_metadata))
    tags.extend(self._CheckUncommitted(files_with_metadata))
    tags.extend(self._CheckFilenames(files_with_metadata))
    return tags



