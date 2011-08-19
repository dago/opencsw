# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = mtwrite
VERSION = r100528
CATEGORIES = lib

DESCRIPTION = Library to enable tar and unzip to write multiple files in parallel
define BLURB
endef

MASTER_SITES = http://www.maier-komor.de/mtwrite/
DISTFILES  = $(NAME)-$(VERSION).tgz

#PATCHFILES += 0002-Hardcode-library-position.patch

VENDOR_URL = http://www.maier-komor.de/mtwrite.html

LICENSE = lgpl.txt

CONFIGURE_SCRIPTS =

EXTRA_CFLAGS = -G -g -mt
EXTRA_LDFLAGS = -zinitarray=init -lthread -ldl -lrt -lumem

BUILD_OVERRIDE_VARS = CC CFLAGS LDFLAGS
BUILD_OVERRIDE_VAR_CC = $(CC)
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)
BUILD_OVERRIDE_VAR_LDFLAGS = $(LDFLAGS)

TEST_SCRIPTS =

INSTALL_OVERRIDE_DIRS = PREFIX
PREFIX=$(prefix)

# This is the intended shared library name. As it is not meant for use with
# LD_LIBRARY_PATH only this is ok.
CHECKPKG_OVERRIDES_CSWmtwrite += soname-equals-filename|file=/opt/csw/lib/mtwrite.so

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/local/lib,$(libdir),' \
		$(DESTDIR)$(mandir)/man3/mtwrite.3
