# $Id
: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tokyocabinet
VERSION = 1.4.47
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Tokyo Cabinet is a library of routines for managing a database.

define BLURB
        Tokyo Cabinet is a library of routines for managing a database. The database is a 
        simple data file containing records, each is a pair of a key and a value. 
        Every key and value is serial bytes with variable length. Both binary data and 
        character string can be used as a key and a value. There is neither concept of 
        data tables nor data types. Records are organized in hash table, B+ tree, 
        or fixed-length array.
endef

MASTER_SITES = http://fallabs.com/tokyocabinet/
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS) 
GARCOMPILER = GCC4
BUILD64 = 1

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
SKIP_MODULATIONS = isa-sparcv8


EXTRA_CPPFLAGS += -DLOG_PERROR=0x00
EXTRA_CPPFLAGS += -D__EXTENSIONS__

PACKAGES += CSWlibtokyocabinet9
PACKAGES += CSWtokyocabinet9
PACKAGES += CSWtokyocabinet-dev

SPKG_DESC_CSWtokyocabinet9 = Tokyo Cabinet shared library

CATALOGNAME_CSWlibtokyocabinet9 = libtokyocabinet9
CATALOGNAME_CSWtokyocabinet-dev = tokyocabinet_dev

RUNTIME_DEP_PKGS_CSWlibtokyocabinet9 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibtokyocabinet9 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibtokyocabinet9 += CSWlibz1
RUNTIME_DEP_PKGS_CSWtokyocabinet-dev += CSWlibtokyocabinet9
RUNTIME_DEP_PKGS_CSWtokyocabinet += CSWlibtokyocabinet9
RUNTIME_DEP_PKGS_CSWtokyocabinet9 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWtokyocabinet9 += CSWlibtokyocabinet9
RUNTIME_DEP_PKGS_CSWtokyocabinet9 += CSWlibz1
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += surplus-dependency|CSWlibtokyocabinet9
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += surplus-dependency|CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += file-with-bad-content|/usr/local|root/opt/csw/share/tokyocabinet/doc/spex-ja.html
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += file-with-bad-content|/usr/local|root/opt/csw/share/tokyocabinet/doc/spex-en.html
CHECKPKG_OVERRIDES_CSWtokyocabinet9 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/tokyocabinet.3

PKGFILES_CSWlibtokyocabinet9 += $(call baseisadirs,$(libdir),libtokyocabinet\.so\.9\.10\.0)
PKGFILES_CSWlibtokyocabinet9 += $(call baseisadirs,$(libdir),libtokyocabinet\.so\.9(\.\d+)*)
PKGFILES_CSWtokyocabinet-dev += /opt/csw/lib/sparcv9/libtokyocabinet.so

SPKG_DESC_CSWlibtokyocabinet9 += $(DESCRIPTION), libtokyocabinet.so.9
SPKG_DESC_CSWtokyocabinet-dev += $(DESCRIPTION), development files

include gar/category.mk

PATH:=/opt/csw/gnu:$(PATH)
