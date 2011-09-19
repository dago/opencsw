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
#GARFLAVOR=DBG
GARCOMPILER = GNU
BUILD64 = 1
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
ARCHALL = 1
SKIP_MODULATIONS = isa-sparcv8
EXTRA_CPPFLAGS += -DLOG_PERROR=0x00
EXTRA_CPPFLAGS += -D__EXTENSIONS__
RUNTIME_DEP_PKGS_CSWtokyocabinet += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWtokyocabinet += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWtokyocabinet += CSWlibz1
DEP_PKGS += CSWcommon
DEP_PKGS += CSWx11common
DEP_PKGS += CSWlibpthreadstubs

PACKAGES += CSWlibtokyocabinet9
CATALOGNAME_CSWlibtokyocabinet9 = libtokyocabinet9
PKGFILES_CSWlibtokyocabinet9 += $(call baseisadirs,$(libdir),libtokyocabinet\.so\.9\.10\.0)
PKGFILES_CSWlibtokyocabinet9 += $(call baseisadirs,$(libdir),libtokyocabinet\.so\.9(\.\d+)*)
SPKG_DESC_CSWlibtokyocabinet9 += $(DESCRIPTION), libtokyocabinet.so.9
RUNTIME_DEP_PKGS_CSWtokyocabinet += CSWlibtokyocabinet9
PACKAGES += CSWtokyocabinet-dev
CATALOGNAME_CSWtokyocabinet-dev = tokyocabinet_dev
SPKG_DESC_CSWtokyocabinet-dev += $(DESCRIPTION), development files
PKGFILES_CSWtokyocabinet-dev += /opt/csw/lib/sparcv9/libtokyocabinet.so

#CHECKPKG_OVERRIDES_CSWtokyocabinet += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/sparcv9/libtokyocabinet.so
#CHECKPKG_OVERRIDES_CSWtokyocabinet += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/libtokyocabinet.so.9.10.0|soname=libtokyocabinet.so.9|pkgname=CSWtokyocabinet|expected=CSWlibtokyocabinet9
#CHECKPKG_OVERRIDES_CSWtokyocabinet += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/sparcv9/libtokyocabinet.so

include gar/category.mk

PATH:=/opt/csw/gnu:$(PATH)

