NAME = rcs
VERSION = 5.9.1
GARTYPE = v2

DESCRIPTION = GNU Revision Control System
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz

PATCHFILES += 0001-sh-bails-out-if-returncode-of-grep-is-1.patch

VENDOR_URL = http://www.gnu.org/software/rcs/

PACKAGES += CSWrcs
SPKG_DESC_CSWrcs = GNU Revision Control System
# PKGFILES is catchall
# We need this for gdiff and gdiff3
RUNTIME_DEP_PKGS_CSWrcs = CSWdiffutils
CHECKPKG_OVERRIDES_CSWrcs += surplus-dependency|CSWdiffutilsr = $(mandir)/man5

DIFF = $(bindir)/gdiff
DIFF3 = # Every kind of -xO* leads to this strange error in Sun Studio 12 or even 12.3:
#   cg error (as) : location counter not on word boundary
OPT_FLAGS_SOS == $(bindir)/gdiff3

NORUNPATH = 1
CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --with-diffutilx man1dir man5dir
BUILD_OVERRIDE_DIRS = DIFF DIFF3

includ