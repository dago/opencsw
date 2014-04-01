NAME = rcs
VERSION = 5.9.2
GARTYPE = v2

DESCRIPTION = GNU Revision Control System
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

VENDOR_URL = http://www.gnu.org/software/rcs/

PACKAGES += CSWrcs
SPKG_DESC_CSWrcs = GNU Revision Control System
# PKGFILES is catchall
# We need this for gdiff and gdiff3
RUNTIME_DEP_PKGS_CSWrcs = CSWdiffutils
CHECKPKG_OVERRIDES_CSWrcs += surplus-dependency|CSWdiffutilsr = $(mandir)/man5

DIFF = $(bindir)/gdiff
DIFF3 = # Sun Studio results in strange errors as reported in
#   https://www.opencsw.org/mantis/view.php?id=5159
GARCOMPILER = GNU= $(bindir)/gdiff3

NORUNPATH = 1
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += BUILD_OVERRIDE_DIRS = DIFF DIFF3

include gar/category.mk
