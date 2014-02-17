"""A collection of utility functions, which don't belong elsewhere."""
import copy
import logging
import magic
import os
import re

from lib.python import common_constants
from lib.python import errors
from lib.python import ldd_emul
from lib.python import representations
from lib.python import sharedlib_utils
from lib.python import shell
from lib.python.collect_binary_elfinfo import ElfExtractor


ROOT_RE = re.compile(r"^(reloc|root)/")


class MimeTypeError(errors.Error):
  """A problem with file's mime type."""


def StripRe(string_to_strip, strip_re):
  """Strips a string of a given pattern."""
  return re.sub(strip_re, "", string_to_strip)


class FileMagic(object):
  """Libmagic sometimes returns None, which I think is a bug.
  Trying to come up with a way to work around that.  It might not even be
  very helpful, but at least detects the issue and tries to work around it.
  """

  def __init__(self):
    self.cookie_count = 0
    self._magic_cookie = None

  def Close(self):
    if self._magic_cookie is not None:
      self._magic_cookie.close()
      self._magic_cookie = None

  @property
  def magic_cookie(self):
    if not self._magic_cookie:
      self._magic_cookie = magic.open(self.cookie_count)
      self.cookie_count += 1
      self._magic_cookie.load()
      if "MAGIC_MIME" in dir(magic):
        flag = magic.MAGIC_MIME
      elif "MIME" in dir(magic):
        flag = magic.MIME
      self._magic_cookie.setflags(flag)
    return self._magic_cookie

  def GetFileMimeType(self, full_path):
    logging.debug("GetFileMimeType(%r)", full_path)
    mime = self.magic_cookie.file(full_path)
    if not mime:
      raise MimeTypeError(
          "libmagic has failed to return the mime type of %r." % (full_path))
    return mime


def GetFileMetadata(file_magic, base_dir, file_path):
  full_path = unicode(os.path.join(base_dir, file_path))
  if not os.access(full_path, os.R_OK):
    return representations.FileMetadata(file_path, None, None)
  file_info_path = StripRe(file_path, ROOT_RE)
  file_info_mime_type = file_magic.GetFileMimeType(full_path)
  if base_dir:
    file_info_path = os.path.join(base_dir, file_info_path)
  if not file_info_mime_type:
    logging.error("Could not establish the mime type of %s",
                  full_path)
    # We can't allow checkpkg to miss binaries. If we can establish the
    # mime type of a file, we need to fail. Unfortunately, libmagic
    # fails for many files in /opt/csw/share, so we are forced to
    # whitelist them. (Or fix libmagic...)
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
    if "/opt/csw/share" in full_path:
      file_info_mime_type = "application/octet-stream; fallback"
      logging.error(msg)
    else:
      raise MimeTypeError(msg)
  if sharedlib_utils.IsBinary({"mime_type": file_info_mime_type}, check_consistency=False):
    elffile = ElfExtractor(full_path)
    file_info_machine_id = elffile.GetMachineIdOfBinary()
  else:
    file_info_machine_id = None
  return representations.FileMetadata(
      file_path, file_info_mime_type, file_info_machine_id)

def GetBinaryDumpInfo(binary_abs_path, binary):
  binary_base_name = os.path.basename(binary)
  elf_extractor = ElfExtractor(binary_abs_path)
  binary_dump_info = elf_extractor.CollectBinaryDumpinfo()

  runpath_to_save = []
  if binary_dump_info['runpath']:
      runpath_to_save.extend(binary_dump_info['runpath'])
  elif binary_dump_info['rpath']:
      runpath_to_save.extend(binary_dump_info['rpath'])

  # Converting runpath and sonames to tuples, which is a hashable data
  # type and can function as a key in a dict.
  binary_dump_info = representations.BinaryDumpInfo(
          binary, binary_base_name,
          binary_dump_info['soname'],
          tuple(binary_dump_info['needed_sonames']),
          tuple(runpath_to_save),
          (binary_dump_info['runpath'] == binary_dump_info['rpath']),
          bool(binary_dump_info['rpath']),
          bool(binary_dump_info['runpath']),
          )

  return binary_dump_info
