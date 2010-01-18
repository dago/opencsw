GARNAME = libtasn1
GARVERSION = 2.4
CATEGORIES = lib

DESCRIPTION = GNU ASN1 library
define BLURB
  Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and some other packages.
  It was written by Fabio Fiorina, and has been shipped as part of GnuTLS for some
  time but is now a proper GNU package.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/gnutls/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS =

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static

TEST_TARGET = check

include gar/category.mk

