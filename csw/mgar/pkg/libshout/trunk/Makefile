NAME = libshout
VERSION = 2.2.2
CATEGORIES = lib

DESCRIPTION = Icecast library
define BLURB
endef

MASTER_SITES = http://downloads.us.xiph.org/releases/libshout/
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWlibshout3
SPKG_DESC_CSWlibshout3 = Icecast library, libshout.so.3
PKGFILES_CSWlibshout3 = $(call pkgfiles_lib,libshout.so.3)
RUNTIME_DEP_PKGS_CSWlibshout3 += CSWlibogg0
RUNTIME_DEP_PKGS_CSWlibshout3 += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWlibshout3 += CSWlibtheora0
OBSOLETED_BY_CSWlibshout3 = CSWlibshout

PACKAGES += CSWlibshout-dev
SPKG_DESC_CSWlibshout-dev = Development files for libshout.so.3
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibshout-dev = CSWlibshout3

BUILD64 = 1

#         GAR default: -xO3 -xarch=v8 -I/opt/csw/include
# Configure hardwired: -xO4 -fast -w -fsimple -native -xcg92
BUILD_ARGS = CFLAGS="-xO4 -fsimple -native -xcg92 $(filter -m% -xarch=% -I%,$(CFLAGS))"

include gar/category.mk

post-extract-modulated:
	perl -pi \
		-e 's,/usr/local,$(prefix),' \
		$(WORKSRC)/m4/shout.m4
