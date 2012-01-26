NAME = Tk
VERSION = 804.028
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SREZIC

DESCRIPTION = A Graphical User Interface ToolKit perl module
define BLURB
  In writing the perl Tk extension, the goals were to provide a complete
  interface to the latest production version of John Ousterhout's Tk, while
  providing an Object Oriented interface to perl code.
endef

PACKAGES = CSWpmtk
CATALOGNAME = pm_tk

RUNTIME_DEP_PKGS = CSWjpeg CSWpng CSWzlib

# Use Solaris zlib/png/jpeg
#PATCHFILES = syslibs.diff

# Fix problems with ISO646 mapping to 'US-ASCII'
PATCHFILES += nl_langinfo.diff

include gar/category.mk
