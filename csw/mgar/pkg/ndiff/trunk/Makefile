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
  It also tells you by how much they differ. 
endef

MASTER_SITES = ftp://ftp.math.utah.edu/pub/misc/
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-fixed-make-install-target.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWndiff += CSWlibgmp
BUILD_DEP_PKGS = 

VENDOR_URL = http://www.math.utah.edu/~beebe/software/ndiff/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

