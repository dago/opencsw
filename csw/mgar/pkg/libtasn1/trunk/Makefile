NAME = libtasn1
VERSION = 2.9
CATEGORIES = lib

DESCRIPTION = GNU ASN1 Library
define BLURB
  Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and some other packages.
  It was written by Fabio Fiorina, and has been shipped as part of GnuTLS for some
  time but is now a proper GNU package.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnu.org/software/gnutls/

PACKAGES += CSWlibtasn1-3
SPKG_DESC_CSWlibtasn1-3 = GNU ASN 1 library, libtasn1.so.3
PKGFILES_CSWlibtasn1-3 = $(call pkgfiles_lib,libtasn1.so.3)

PACKAGES += CSWlibtasn1-dev
SPKG_DESC_CSWlibtasn1-dev = Development files for libtasn1.so.3
PKGFILES_CSWlibtasn1-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibtasn1-dev = CSWlibtasn1-3
OBSOLETED_BY_CSWlibtasn1-dev += CSWlibtasn1devel
CATALOGNAME_CSWlibtasn1devel = libtasn1_devel_stub

PACKAGES += CSWlibtasn1-utils
SPKG_DESC_CSWlibtasn1-utils = GNU ASN1 utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtasn1-utils = CSWlibtasn1-3
OBSOLETED_BY_CSWlibtasn1-utils = CSWlibtasn1

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

BUILD64 = 1

include gar/category.mk

