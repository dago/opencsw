import package
import os
import re
import logging
import hachoir_parser as hp
import sharedlib_utils
import magic

"""This file isolates code dependent on hachoir parser.

hachoir parser takes quite a while to import.
"""

# Suppress unhelpful warnings
# http://bitbucket.org/haypo/hachoir/issue/23
import hachoir_core.config
hachoir_core.config.quiet = True

class InspectivePackage(package.DirectoryFormatPackage):
  """Extends DirectoryFormatPackage to allow package inspection."""

  def GetFilesMetadata(self):
    """Returns a data structure with all the files plus their metadata.

    [
      {
        "path": ...,
        "mime_type": ...,
      },
    ]
    """
    if not self.files_metadata:
      self.CheckPkgpathExists()
      self.files_metadata = []
      files_root = os.path.join(self.directory, "root")
      all_files = self.GetAllFilePaths()
      def StripRe(x, strip_re):
        return re.sub(strip_re, "", x)
      root_re = re.compile(r"^root/")
      file_magic = FileMagic()
      for file_path in all_files:
        full_path = unicode(self.MakeAbsolutePath(file_path))
        file_info = {
            "path": StripRe(file_path, root_re),
            "mime_type": file_magic.GetFileMimeType(full_path)
        }
        if not file_info["mime_type"]:
          logging.error("Could not establish the mime type of %s",
                        full_path)
          # We really don't want that, as it misses binaries.
          msg = (
              "It was not possible to establish the mime type of %s.  "
              "It's a known problem which occurs when indexing a large "
              "number of packages in a single run.  "
              "It's probably caused by a bug in libmagic, or a bug in "
              "libmagic Python bindings. "
              "Currently, there is no fix for it.  "
              "You have to restart your process - it "
              "will probably finish successfully when do you that."
              % full_path)
          raise package.PackageError(msg)
        if sharedlib_utils.IsBinary(file_info):
          parser = hp.createParser(full_path)
          if not parser:
            logging.warning("Can't parse file %s", file_path)
          else:
            file_info["mime_type_by_hachoir"] = parser.mime_type
            machine_id = parser["/header/machine"].value
            file_info["machine_id"] = machine_id
            file_info["endian"] = parser["/header/endian"].display
        self.files_metadata.append(file_info)
    return self.files_metadata

  def ListBinaries(self):
    """Lists all the binaries from a given package.

    Original checkpkg code:

    #########################################
    # find all executables and dynamic libs,and list their filenames.
    listbinaries() {
      if [ ! -d $1 ] ; then
        print errmsg $1 not a directory
        rm -rf $EXTRACTDIR
        exit 1
      fi
      find $1 -print | xargs file |grep ELF |nawk -F: '{print $1}'
    }

    Returns a list of absolute paths.

    Now that there are files_metadata, this function can safely go away, once
    all its callers are modified to use files_metadata instead.
    """
    if self.binaries is None:
      self.CheckPkgpathExists()
      files_metadata = self.GetFilesMetadata()
      self.binaries = []
      # The nested for-loop looks inefficient.
      for file_info in files_metadata:
        if sharedlib_utils.IsBinary(file_info):
          self.binaries.append(file_info["path"])
      self.binaries.sort()
    return self.binaries

  def GetAllFilePaths(self):
    """Returns a list of all paths from the package."""
    if not self.file_paths:
      self.CheckPkgpathExists()
      remove_prefix = "%s/" % self.pkgpath
      self.file_paths = []
      for root, dirs, files in os.walk(os.path.join(self.pkgpath, "root")):
        full_paths = [os.path.join(root, f) for f in files]
        self.file_paths.extend([f.replace(remove_prefix, "") for f in full_paths])
    return self.file_paths


class FileMagic(object):
  """Libmagic sometimes returns None, which I think is a bug.
  Trying to come up with a way to work around that.  It might not even be
  very helpful, but at least detects the issue and tries to work around it.
  """

  def __init__(self):
    self.cookie_count = 0
    self.magic_cookie = None

  def _GetCookie(self):
    magic_cookie = magic.open(self.cookie_count)
    self.cookie_count += 1
    magic_cookie.load()
    magic_cookie.setflags(magic.MAGIC_MIME)
    return magic_cookie

  def _LazyInit(self):
    if not self.magic_cookie:
      self.magic_cookie = self._GetCookie()

  def GetFileMimeType(self, full_path):
    """Trying to run magic.file() a few times, not accepting None."""
    self._LazyInit()
    mime = None
    for i in xrange(10):
      mime = self.magic_cookie.file(full_path)
      if mime:
        break;
      else:
        # Returned mime is null. Re-initializing the cookie and trying again.
        logging.error("magic_cookie.file(%s) returned None. Retrying.",
                      full_path)
        self.magic_cookie = self._GetCookie()
    return mime


class InspectiveCswSrv4File(package.CswSrv4File):
  """Allows to get the inspective version of the dir format pkg."""

  # The presence of this method makes it explicit that we want an inspective
  # version of the directory format package.
  def GetInspectivePkg(self):
    return self.GetDirFormatPkg()

  def GetDirFormatClass(self):
    return InspectivePackage
