# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tokyocabinet
VERSION = 1.4.47
GARTYPE = v2
CATEGORIES = lib
GARCOMPILER = SOS12U1

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = Brief description
define BLURB
  Tokyo Cabinet is a library of routines for managing a database. The 
  database is a simple data file containing records, each is a pair
  of a key and a value. Every key and value is serial bytes with variable
  length. Both binary data and character string can be used as a key and
  a value. There is neither concept of data tables nor data types. Records
  are organized in hash table, B+ tree, or fixed-length array.
endef

MASTER_SITES = http://fallabs.com/tokyocabinet
DISTFILES  = $(DISTNAME).tar.gz

# Adjust man page
PATCHFILES += 0003-adjust-man-page-for-csw.patch

# This patch also goes hand in hand with TEST_ARGS further below.
PATCHFILES += 0002-Huge-Makefile.in-patch.patch

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES  = CSWlibtokyocabinet9
SPKG_DESC_CSWlibtokyocabinet9 = Tokyocabinet - library
PKGFILES_CSWlibtokyocabinet9 = $(call pkgfiles_lib,libtokyocabinet.so.9)
RUNTIME_DEP_PKGS_CSWlibtokyocabinet9 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibtokyocabinet9 += CSWlibz1
CHECKPKG_OVERRIDES_CSWlibtokyocabinet9 += file-with-bad-content|/usr/local|root/opt/csw/lib/libtokyocabinet.so.9.10.0
CHECKPKG_OVERRIDES_CSWlibtokyocabinet9 += file-with-bad-content|/usr/local|root/opt/csw/lib/sparcv9/libtokyocabinet.so.9.10.0

PACKAGES += CSWlibtokyocabinet-dev
SPKG_DESC_CSWlibtokyocabinet-dev = Tokyocabinet - development files
PKGFILES_CSWlibtokyocabinet-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibtokyocabinet-dev += .*/doc/libtokyocabinet_dev/tokyocabinet.idl
RUNTIME_DEP_PKGS_CSWlibtokyocabinet-dev  = CSWlibtokyocabinet9

PACKAGES += CSWtokyocabinet-bin
SPKG_DESC_CSWtokyocabinet-bin = Tokyocabinet - utilities
PKGFILES_CSWtokyocabinet-bin  = .*/bin/.*
PKGFILES_CSWtokyocabinet-bin += .*/man/man1/.*
RUNTIME_DEP_PKGS_CSWtokyocabinet-bin  = CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWtokyocabinet-bin += CSWlibz1
RUNTIME_DEP_PKGS_CSWtokyocabinet-bin += CSWlibtokyocabinet9

PACKAGES += CSWtokyocabinet-doc
ARCHALL_CSWtokyocabinet-doc = 1
SPKG_DESC_CSWtokyocabinet-doc = Tokyocabinet - documentation
PKGFILES_CSWtokyocabinet-doc  = .*/doc/tokyocabinet_doc/.*
# That's ok, it's in the howto build section
CHECKPKG_OVERRIDES_CSWtokyocabinet-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/tokyocabinet_doc/doc/spex-en.html
CHECKPKG_OVERRIDES_CSWtokyocabinet-doc += file-with-bad-content|/usr/local|root/opt/csw/share/doc/tokyocabinet_doc/doc/spex-ja.html

BUILD64 = 1

EXTRA_CFLAGS-sparc = -xcode=pic13
EXTRA_CFLAGS-i386  = -Kpic

EXTRA_CFLAGS	= -xc99=all $(EXTRA_CFLAGS-$(GARCH))
EXTRA_CPPFLAGS	= -DPIC

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-bzip=$(prefix)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-shared

TEST_ARGS += WORKDIR=$(abspath $(WORKDIR)/$(NAME)-$(VERSION))

include gar/category.mk

post-merge:
	install -d $(PKGROOT)$(docdir)/libtokyocabinet_dev
	install -d $(PKGROOT)$(docdir)/tokyocabinet_doc
	mv $(PKGROOT)$(sharedstatedir)/tokyocabinet/tokyocabinet.idl $(PKGROOT)$(docdir)/libtokyocabinet_dev/
	mv $(PKGROOT)$(sharedstatedir)/tokyocabinet/COPYING \
		$(PKGROOT)$(sharedstatedir)/tokyocabinet/ChangeLog \
		$(PKGROOT)$(docdir)/libtokyocabinet_dev/
	mv $(PKGROOT)$(sharedstatedir)/tokyocabinet/doc $(PKGROOT)$(docdir)/tokyocabinet_doc/
	rm -rf $(PKGROOT)$(sharedstatedir)/tokyocabinet
	@$(MAKECOOKIE)
