# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mosh
VERSION = 1.1.3
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Mobile shell

MASTER_SITES = https://github.com/downloads/keithw/mosh/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Test-on-inttypes.h-in-addition-to-stdint.h-and-don-t.patch
PATCHFILES += 0002-Various-Solaris-fixes.patch

# Functions betoh64 from http://licq.sourcearchive.com/documentation/1.3.8/licq__byteorder_8h-source.html

PACKAGES += CSWmosh
SPKG_DESC_CSWmypkg = Mobile shell

# boost gxx is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# See https://forums.oracle.com/forums/thread.jspa?threadID=2019232
EXTRA_CPPFLAGS += -D__aligned__=aligned

GARCOMPILER = GCC4

EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += $(prefix)/gxx/lib

include gar/category.mk

post-patch-modulated:
	-cd $(WORKSRC) && /opt/csw/bin/autoreconf -fi
	@$(MAKECOOKIE)
