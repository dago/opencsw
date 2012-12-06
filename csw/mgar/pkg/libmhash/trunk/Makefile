NAME = mhash
VERSION = 0.9.9.9
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A uniform interface to a large number of hash algorithms
define BLURB
  Mhash is a free (under GNU Lesser GPL) library which provides a uniform
  interface to a large number of hash algorithms. These algorithms can be
  used to compute checksums, message digests, and other signatures.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

UFILES_REGEX = $(NAME)-(\d+(?:\VENDOR_.bz2

SPKG_SOURCEURL = http://mhash.sourceforge.net/

EXTRA_CPPFLAGS = -D__const=const

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

# sparcv9 compile fails with optimization beyond -xO1 at HAVAL256: FAIL: frag_test
# Please see files/README for details.

ifeq ($(ISA),sparcv9)
OPT_FLAGS_SOS = -xO1
endif

CONFIGURE_ARGS = $(DIRPATHS)

# Always run testsuite as the code is prone to opt
PACKAGES += CSWlibmhash2
SPKG_DESC_CSWlibmhash2 = A uniform interface to a large number of hash algorithms, libmhash.so.2
PKGFILES_CSWlibmhash2 += $(call pkgfiles_lib,libmhash.so.2)
OBSOLETED_BY_CSWlibmhash2 += CSWlibmhash

PACKAGES += CSWlibmhash-dev
SPKG_DESC_CSWlibmhash-dev = Development files for libmash.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibmhash-dev += CSWlibmhash2GES = CSWlibmhash

include gar/category.mk

# Don't include the most common defines. In general it is a bad idea to include
# the config file as it may collide with the config file from the main package
# using libmhash.
post-install-modulated:
	perl -pi -e 's,^(#define (?:PACKAGE|PACKAGE_BUGREPORT|PACKAGE_NAME|PACKAGE_STRING|PACKAGE_TARNAME|PACKAGE_VERSION|VERSION) .*),/* \1 */,' \
		$(DESTDIR)$(includedir)/mutils/mhash_config.h
