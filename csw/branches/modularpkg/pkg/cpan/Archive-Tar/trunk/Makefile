GARNAME = Archive-Tar
GARVERSION = 1.30
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = module for manipulations of tar archives
define BLURB
  Archive::Tar provides an object oriented mechanism for handling tar files.
  It provides class methods for quick and easy files handling while also
  allowing for the creation of tar file objects for custom manipulation. If
  you have the IO::Zlib module installed, Archive::Tar will also support
  compressed or gzipped tar files.
endef

DISTFILES += $(call admfiles,CSWpmarchivetar,depend prototype)

DEPENDS += cpan/IO-Zlib

include gar/category.mk
