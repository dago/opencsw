# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = lrzsz
VERSION = 0.12.20

DESCRIPTION = X/Y/Zmodem suite
define BLURB
endef

MASTER_SITES = http://ohse.de/uwe/releases/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://ohse.de/uwe/software/lrzsz.html

PACKAGES += CSWlrzsz
SPKG_DESC_CSWlrzsz = X/Y/Zmodem suite
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlrzsz += CSWlibintl8

EXTRA_LINKER_FLAGS += -lintl

include gar/category.mk
