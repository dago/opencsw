NAME = libtasn1
VERSION = 3.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU ASN1 Library
define BLURB
  Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and some other packages.
  It was written by Fabio Fiorina, and has been shipped as part of GnuTLS for some
  time but is now a proper GNU package.
endef

MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += http://daily.josefsson.org/libtasn1/
MASTER_SITES += ftp://ftp.hellug.gr/pub/gnutls/libtasn1/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnu.org/software/gnutls/

PACKAGES += CSWlibtasn1-6
SPKG_DESC_CSWlibtasn1-6 = GNU ASN 1 library, libtasn1.so.6
PKGFILES_CSWlibtasn1-6 = $(call pkgfiles_lib,libtasn1.so.6)

PACKAGES += CSWlibtasn1-dev
SPKG_DESC_CSWlibtasn1-dev = Development files for libtasn1.so.6
PKGFILES_CSWlibtasn1-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibtasn1-dev = CSWlibtasn1-6
OBSOLETED_BY_CSWlibtasn1-dev += CSWlibtasn1devel
CATALOGNAME_CSWlibtasn1devel = libtasn1_devel_stub

PACKAGES += CSWlibtasn1-utils
SPKG_DESC_CSWlibtasn1-utils = GNU ASN1 utilities
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibtasn1-utils = CSWlibtasn1-6
OBSOLETED_BY_CSWlibtasn1-utils = CSWlibtasn1

BUILD64_LIBS_ONLY = 1

include gar/category.mk

