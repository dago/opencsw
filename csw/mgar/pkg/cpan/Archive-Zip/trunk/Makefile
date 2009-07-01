GARNAME = Archive-Zip
GARVERSION = 1.30
CATEGORIES = cpan
AUTHOR = ADAMK

DESCRIPTION = Provides an interface to ZIP archive files
define BLURB
  The Archive::Zip module allows a Perl program to create, manipulate, read,
  and write Zip archive files. Zip archives can be created, or you can read
  from existing zip files. Once created, they can be written to files,
  streams, or strings. Members can be added, removed, extracted, replaced,
  rearranged, and enumerated. They can also be renamed or have their dates,
  comments, or other attributes queried or modified. Their data can be
  compressed or uncompressed as needed. Members can be created from members in
  existing Zip files, or from existing directories, files, or strings. This
  module uses the Compress::Zlib library to read and write the compressed
  streams inside the files.
endef

DISTFILES = COPYING

PACKAGES = CSWpmarchivezip
CATALOGNAME = pm_archivezip
ARCHALL = 1

REQUIRED_PKGS = CSWpmcompresszlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

include gar/category.mk
