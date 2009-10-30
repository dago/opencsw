GARNAME = mhash
GARVERSION = 0.9.9.9
CATEGORIES = lib

DESCRIPTION = A uniform interface to a large number of hash algorithms
define BLURB
  Mhash is a free (under GNU Lesser GPL) library which provides a uniform
  interface to a large number of hash algorithms. These algorithms can be
  used to compute checksums, message digests, and other signatures.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://mhash.sourceforge.net/

EXTRA_CPPFLAGS = -D__const=const

BUILD64 = 1
NOISALIST = 1

# sparcv9 compile fails with optimization beyond -xO1 at HAVAL256: FAIL: frag_test
# Please see files/README for details.

ifeq ($(ISA),sparcv9)
OPT_FLAGS_SOS = -xO1
endif

CONFIGURE_ARGS = $(DIRPATHS)

# Always run testsuite as the code is prone to optimization errors
TEST_TARGET = check

PACKAGES = CSWlibmhash

include gar/category.mk

# Don't include the most common defines. In general it is a bad idea to include
# the config file as it may collide with the config file from the main package
# using libmhash.
post-install-modulated:
	perl -pi -e 's,^(#define (?:PACKAGE|PACKAGE_BUGREPORT|PACKAGE_NAME|PACKAGE_STRING|PACKAGE_TARNAME|PACKAGE_VERSION|VERSION) .*),/* \1 */,' \
		$(DESTDIR)$(includedir)/mutils/mhash_config.h
	@$(MAKECOOKIE)

