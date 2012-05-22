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

#PATCHFILES += 0001-Test-on-inttypes.h-in-addition-to-stdint.h-and-don-t.patch
#PATCHFILES += 0002-Various-Solaris-fixes.patch

PATCHFILES += 0001-Hack-around-so-it-compiles-on-Solaris.patch
PATCHFILES += 0001-Do-not-use-libutil.patch

# Functions betoh64 from http://licq.sourcearchive.com/documentation/1.3.8/licq__byteorder_8h-source.html

BUILD_DEP_PKGS += CSWboost-gcc-dev
BUILD_DEP_PKGS += CSWprotobuf-gxx-dev

PACKAGES += CSWmosh
SPKG_DESC_CSWmypkg = Mobile shell
RUNTIME_DEP_PKGS_CSWmosh += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWmosh += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWmosh += CSWlibprotobuf7-gxx
RUNTIME_DEP_PKGS_CSWmosh += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWmosh += CSWlibz1

# boost gxx is only available on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

GARCOMPILER = GCC4

# See https://forums.oracle.com/forums/thread.jspa?threadID=2019232
EXTRA_CPPFLAGS += -D__aligned__=aligned

EXTRA_CONFIGURE_EXPORTS += PROTOC
CONFIGURE_ENV_PROTOC = $(prefix)/gxx/bin/protoc

EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += $(prefix)/gxx/lib

EXTRA_LINKER_FLAGS += -lsocket -lnsl

include gar/category.mk

post-patch-modulated:
	-cd $(WORKSRC) && /opt/csw/bin/autoreconf -fi
	@# These are generated protobuf files, regenerate later
	-cd $(WORKSRC)/src/protobufs && rm -f *.cc *.h
	@$(MAKECOOKIE)
