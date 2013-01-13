# $Id$

NAME = libffi
VERSION = 3.0.9
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A portable foreign function interface library
define BLURB
	FFI stands for Foreign Function Interface. A
	interface is the popular name for the interface that allows codethat allows code 
	written in one language to call code written in 
	The libffi library really only provides the lowest, machine
	dependent layer of a fully featured foreign function interface.
	A layer must exist above libffi that handles type conversions for
	values passed between the two languages.e two languages. 
endef

MASTER_SITES = ftp://sourceware.org/pub/libffi/
SPKG_SOURCEURL = http://sourceware.org/libffi/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
# Not needed unless using SOS compiler
PATCHFILES += Makefile.in.patch
# Not really needed for build, but for SOS compiler using libffi
PATCHFILES += ffi_common.h.patch
PATCHFILES += ffi_target.h.patch
# Fix needed for amd64 using SOS compiler
# found at http://software.intel.com/en-us/forums/showthread.php?t=56652
# originally for icc, but at least get the stuff to compile
PATCHFILES += ffi64.c.patch
PATCHFILES += 0005-libffi.pc-should-point-at-opt-csw-include.patch
PATCHFILES += 0006-Set-libdir-to-opt-csw-lib-ffi.patch

OBSOLETED_BY_CSWlibffi5 = CSWlibffi
OBSOLETED_BY_CSWlibffi5-dev = CSWlibffi
INCOMPATIBLE_PKGS_CSWlibffi5 = CSWlibffi

PACK5
PKGFILES_CSWlibffi5 += $(call baseisadirs,$(libdir),libffi\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibffi5 += $(DESCRIPTION), libffi.so.5

PACKAGES += CSWlibffi-dev
SPKG_DESC_CSWlibffi-dev = $(DESCRIPTION) - developer package
RUNTIME_DEP_PKGS_CSWlibffi-dev += CSWlibffi5*/libffi\.so\.5.*

LICENSE = LICENSE

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS  = $(DIRPATHS)

# Tests fail since they are wri
# But they also fails on 64-bit even when using gcc
#TEST_TARGET = check
TEST_TARGET =ck
TEST_TARGET = 

include gar/category.mk


# v9.S is not needed when building 32-bit
pre-configure-isa-sparcv8:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v9.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake)

# v8.S will not build when building 64-bit
pre-configure-isa-sparcv9:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v8.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake)
	$(MAKECOOKIE)

post-install-modulated:
	rm $(DESTDIR)$(libdir)/libffi.so
	ginstall -m 755 -d $(DESTDIR)$(libdir)/ffi
	ln -s ../libffi.so.5.0.10 $(DESTDIR)$(libdir)/ffi/libffi.so
	ginstall -d -m 755 $(DESTDIR)$(includedir)
	# By default, libffi installer puts include files into a subdirectory under
	# /opt/csw/lib, which makes the header files hard to find.  We're moving
	# them to /opt/csw/include.
	gmv -v $(DESTDIR)$(libdir)/$(NAME)-$(VERSION)/include/* $(DESTDIR)$(includedir)
	rmdir $(DESTDIR)$(libdir)/$(NAME)-$(VERSION)/include
	rmdir $(DESTDIR)$(libdir)/$(NAME)-$(VERSION)