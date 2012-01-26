# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = libical
VERSION = 0.44
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Library that implements the iCal protocols in RFC2445, RFC2446, RFC2447
define BLURB
endef

SF_PROJ = freeassociation
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Fix testsuite until this is resolved:
#   http://sourceforge.net/tracker/?func=detail&aid=2988172&group_id=16077&atid=116077
PATCHFILES = 0001-Use-putenv-instead-of-setenv.patch

# Fix on Solaris x86 only until this is resolved:
#   http://sourceforge.net/tracker/?func=detail&aid=2805395&group_id=16077&atid=116077
# (Patch has been reformatted for homogenous PATCHDIRLEVEL)
PATCHFILES += 0002-libical-icaltz-util-sol10.diff.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://freeassociation.sourceforge.net/

PACKAGES = CSWlibical CSWlibicaldevel

CATALOGNAME_CSWlibical = libical
CATALOGNAME_CSWlibicaldevel = libical_devel

SPKG_DESC_CSWlibical = $(DESCRIPTION)
SPKG_DESC_CSWlibicaldevel = Developer files for libical

RUNTIME_DEP_PKGS_CSWlibicaldevel = CSWlibical

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibicaldevel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibicaldevel += surplus-dependency|CSWlibical

include gar/category.mk
