# $Id$

NAME = mpfr
VERSION = 2.3.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Legacy MPFR version
define BLURB
	The MPFR library is a C library for multiple-precision floating-point 
	computations with correct rounding.
endef

MASTER_SITES = http://www.mpfr.org/mpfr-$(VERSION)/

# For the license file.
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.mpfr.org/

BUILD64 = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)

PACKAGES = CSWlibmpfr
CATALOGNAME_CSWlibmpfr = libmpfr
PKGFILES_CSWlibmpfr += $(call baseisadirs,$(libdir),libmpfr\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibmpfr += $(DESCRIPTION), libmpfr.so.1
RUNTIME_DEP_PKGS_CSWlibmpfr += CSWlibgmp

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS =

# For merging purposes
EXTRA_BUILD_ISAS_sparc = sparcv8plus sparcv8plus+vis 
EXTRA_BUILD_ISAS_i386  = pentium

# It's a legacy package, there's no gain in moving files to libmpfr1.
CHECKPKG_OVERRIDES_CSWlibmpfr += shared-lib-pkgname-mismatch

# It's a legacy library, we aren't recompiling it.
CHECKPKG_OVERRIDES_CSWlibmpfr += bad-rpath-entry|/opt/csw/lib/sparcv8plus+vis|opt/csw/lib/sparcv8plus+vis/libmpfr.so.1.1.1

include gar/category.mk

# Check the binary files into subversion.

# A oneliner to extract the files. Make sure to run it on current10x too,
# because current9x may not have the amd64 files.
# oldlib=libmpfr.so.1.1.1
# for i in $(isalist); do f=/opt/csw/lib/$i/$oldlib; \
# if [ -r ${f} ]; then gcp -v $f \
# ~/src/opencsw/pkg/libmpfr/branches/libmpfr1/files/$oldlib-$i; fi; done
OLDLIB_FILE = libmpfr.so.1.1.1
OLDLIB_SONAME = libmpfr.so.1

post-merge:
	ginstall -m 755 -d $(PKGROOT)$(libdir)
	if [ $(GARCH) = i386 ]; then \
		ginstall -m 755 $(FILEDIR)/$(OLDLIB_FILE)-i386 $(PKGROOT)$(libdir)/$(OLDLIB_FILE); \
		gln -s $(OLDLIB_FILE) $(PKGROOT)$(libdir)/$(OLDLIB_SONAME); \
		for arch in pentium amd64 ; do \
			ginstall -m 755 -d $(PKGROOT)$(libdir)/$$arch; \
			ginstall -m 755 $(FILEDIR)/$(OLDLIB_FILE)-$$arch $(PKGROOT)$(libdir)/$$arch/$(OLDLIB_FILE); \
		  gln -s $(OLDLIB_FILE) $(PKGROOT)$(libdir)/$$arch/$(OLDLIB_SONAME); \
		done; \
	elif [ $(GARCH) = sparc ]; then \
		ginstall -m 755 $(FILEDIR)/$(OLDLIB_FILE)-sparc $(PKGROOT)$(libdir)/$(OLDLIB_FILE); \
		gln -s $(OLDLIB_FILE) $(PKGROOT)$(libdir)/$(OLDLIB_SONAME); \
		for arch in sparcv8 sparcv8plus sparcv8plus+vis sparcv9 ; do \
			ginstall -m 755 -d $(PKGROOT)$(libdir)/$$arch; \
			ginstall -m 755 $(FILEDIR)/$(OLDLIB_FILE)-$$arch $(PKGROOT)$(libdir)/$$arch/$(OLDLIB_FILE); \
		  gln -s $(OLDLIB_FILE) $(PKGROOT)$(libdir)/$$arch/$(OLDLIB_SONAME); \
		done; \
	fi
	@$(MAKECOOKIE)
