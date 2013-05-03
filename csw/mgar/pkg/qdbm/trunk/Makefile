# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = qdbm
VERSION = 1.8.78
GARTYPE = v2
GARCOMPILER = SUN

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386 solaris10-sparc solaris10-i386

DESCRIPTION = QDBM is a library of routines for managing a database.
define BLURB
  QDBM is a library of routines for managing a database. The database
  is a simple data file containing records, each is a pair of a key
  and a value. Every key and value is serial bytes with variable
  length. Both binary dat a and character string can be used as a key
  and a value. There is neither concept of data tables nor data
  types. Records are organized in hash table or B+ tree.
endef

MASTER_SITES = http://fallabs.com/qdbm/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES  = 0000-Adjusting-compiler-flags-for-C-C-libs.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES  = CSWqdbm-bin
SPKG_DESC_CSWqdbm-bin = QDBM - utilities
PKGFILES_CSWqdbm-bin  = .*/bin/.*
PKGFILES_CSWqdbm-bin += .*/man/man1/.*
RUNTIME_DEP_PKGS_CSWqdbm-bin = CSWlibqdbm14

PACKAGES += CSWlibqdbm14
SPKG_DESC_CSWlibqdbm14 = QDBM - library
PKGFILES_CSWlibqdbm14  = $(call baseisadirs,$(libdir),libqdbm\.so\.14(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibqdbm14  = CSWliblzo2-2
RUNTIME_DEP_PKGS_CSWlibqdbm14 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibqdbm14 += CSWlibz1
OBSOLETED_BY_CSWlibqdbm14 = CSWqdbm
CHECKPKG_OVERRIDES_CSWlibqdbm14 += file-with-bad-content|/usr/local|root/opt/csw/lib/libqdbm.so.14.14.0
CHECKPKG_OVERRIDES_CSWlibqdbm14 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libqdbm.so.14.14.0
CHECKPKG_OVERRIDES_CSWlibqdbm14 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libqdbm.so.14.14.0

PACKAGES += CSWlibqdbm-dev
SPKG_DESC_CSWlibqdbm-dev = QDBM - development files
RUNTIME_DEP_PKGS_CSWlibqdbm-dev = CSWlibqdbm14

BUILD_DEP_PKGS  = CSWlibbz2-dev
BUILD_DEP_PKGS += CSWliblzo-dev 
BUILD_DEP_PKGS += CSWlibz-dev

BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pthread 
CONFIGURE_ARGS += --enable-zlib
CONFIGURE_ARGS += --enable-lzo
CONFIGURE_ARGS += --enable-bzip

include gar/category.mk

post-install-modulated:
	rm $(DESTDIR)$(libdir)/libqdbm.so
	rm $(DESTDIR)$(libdir)/libqdbm.so.14
	cd $(DESTDIR)$(libdir) ; \
	ln -s libqdbm.so.14.14.0 libqdbm.so.14 ; \
	ln -s libqdbm.so.14 libqdbm.so
	@$(MAKECOOKIE)

post-merge: merge-doc

merge-doc:
	if [ -d $(PKGROOT)$(prefix)/share/qdbm ] ; then\
		[ ! -d $(PKGROOT)$(docdir)/qdbm ] && mkdir -p $(PKGROOT)$(docdir)/qdbm ; \
		mv $(PKGROOT)$(prefix)/share/qdbm/* $(PKGROOT)/$(docdir)/qdbm/ ; \
		rmdir $(PKGROOT)$(prefix)/share/qdbm ; \
	fi
	@$(MAKECOOKIE)
