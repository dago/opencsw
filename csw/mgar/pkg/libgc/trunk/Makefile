NAME = libgc
VERSION = 7.1
CATEGORIES = lib

DESCRIPTION = A garbage collector for C and C++
define BLURB
	The Boehm-Demers-Weiser conservative garbage collector can be used as a
	garbage collecting replacement for C malloc or C++ new. It allows you to
	allocate memory basically as you normally would, without explicitly
	deallocating memory that is no longer useful. The collector automatically
	recycles memory when it determines that it can no longer be otherwise
	accessed.
endef

MASTER_SITES = http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/
DISTNAME = gc-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.hpl.hp.com/personal/Hans_Boehm/gc/

LICENSE = README.QUICK

PACKAGES += CSWlibcord1
SPKG_DESC_CSWlibcord1 = A garbage collector for C and C++, libcord.so.1
PKGFILES_CSWlibcord1 += $(call pkgfiles_lib,libcord.so.1)
RUNTIME_DEP_PKGS_CSWlibcord1 += CSWlibgc1
OBSOLETED_BY_CSWlibcord1 += CSWlibgc

PACKAGES += CSWlibgc1
SPKG_DESC_CSWlibgc1 = A garbage collector for C and C++, libgc.so.1
PKGFILES_CSWlibgc1 += $(call pkgfiles_lib,libgc.so.1)
OBSOLETED_BY_CSWlibgc1 += CSWlibgc

PACKAGES += CSWlibgc-dev
SPKG_DESC_CSWlibgc-dev = Development files for libgc.so.1 and libcord.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibgc-dev += CSWlibcord1
RUNTIME_DEP_PKGS_CSWlibgc-dev += CSWlibgc1

# This is just docs, ignore for now
CHECKPKG_OVERRIDES_CSWlibgc-dev += file-with-bad-content|/usr/local|root/opt/csw/share/gc/README.autoconf

# One test is failing on amd64, disable for now:
#   FAIL: gctest
# The bugreport has been posted on
#   http://www.hpl.hp.com/hosted/linux/mail-archives/gc/2012-January/004904.html
# BUILD64_LIBS_ONLY = 1

include gar/category.mk
