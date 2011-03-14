# $Id$
NAME = libkate
VERSION = 0.3.8
CATEGORIES = lib

DESCRIPTION = A karaoke and text codec for embedding in ogg
define BLURB
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Reformat-null-test-string.patch
PATCHFILES += 0002-Use-inttypes-when-stdint-is-not-available.patch

VENDOR_URL = http://code.google.com/p/libkate/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-configure-modulated:
	perl -pi -e 's,-Wall -W,,g' \
		$(WORKSRC)/Makefile \
		$(WORKSRC)/tools/Makefile
	
