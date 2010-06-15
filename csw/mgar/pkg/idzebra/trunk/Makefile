# $Id$
GARNAME = idzebra
GARVERSION = 2.0.43
CATEGORIES = lib

DESCRIPTION = A high-performance, general-purpose structured text indexing and retrieval engine
define BLURB
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/zebra/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE.zebra

DEP_PKGS = CSWyaz CSWgcrypt CSWexpat CSWlibxml2 CSWlibxslt CSWbzip2 CSWgpgerr CSWiconv CSWtcl CSWzlib

VENDOR_URL = http://www.indexdata.com/zebra

# Just wait a _little_ longer until yaz is ready in 64 bit, which itself needs libicu in 64 bit
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
