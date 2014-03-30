NAME = ndiff
VERSION = 2.00
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Compare putatively similar files, ignoring small numeric differences
define BLURB
  Ndiff assumes that you have two text files containing numerical values,
  and the two files are expected to be identical, or at least numerically
  similar. ndiff allows you to specify absolute and/or relative error
  tolerances for differences between numerical values in the two files,
  and then reports only the lines with values exceeding those tolerances.
  It also tells you by ho much they differ. 
endef

MASTER_SITES = ftp://ftp.math.utah.edu/pub/misc/
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-fixed-make-insPACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

RUNTIME_DEP_PKGS_CSWndiff += CSWlibgmp10
BUILD_DEP_PKGS =

# The test suite seems to be broken
SKIPTEST = 1p
BUILD_DEP_PKGS = 

VENDOR_URL = http://www.math.utah.edu/~beebe/software/ndiff/

CONFIGURE_ARGS = $(DIRPATHS)

includ